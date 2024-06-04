import requests
import json
import urllib
from azure.identity import DeviceCodeCredential
from pyspark.sql import SparkSession
import base64

from . import spark_client, databricks_client

class TenantClient:

    """
    A client for interacting with a specific tenant on a Kobai instance.
    """

    def __init__(self, tenant_name: str, tenant_id: str, uri: str, schema: str):

        """
        Initialize the TenantClient

        Parameters:
        tenant_name (str): The name of the tenant to access, as seen in the Kobai Studio UI.
        tenant_id (str): The numeric identifier for the tenant.
        uri (str): The base URI of the Kobai instance. (eg: "https://example.kobai.io")
        schema (str): The catalog-qualified schema used by Kobai Saturn for this tenant.
        """
        
        self.token = ""
        self.tenant_name = tenant_name
        self.uri = uri
        self.schema = schema
        self.id = tenant_id
        self.tenant_json = {}

########################################
# MS Entra Auth
########################################

    def authenticate(self, client_id: str, tenant_id: str):

        """
        Authenticate the TenantClient with the Kobai instance. Returns nothing, but stores bearer token in client.

        Limitations:
        Currently supports only authentication via Microsoft Entra (AzureAD) using DecideCode OAuth flow.

        Parameters:
        client_id (str): Client ID or Application ID from app registration with IDM.
        tenant_id (str): Tenant ID or Directory ID for IDM.
        """

        credential = DeviceCodeCredential(client_id=client_id, tenant_id=tenant_id)

        access = credential.authenticate()

        oauth_token = access.serialize()
        user_name = json.loads(access.serialize())["username"]

        tenants_url = self.uri + '/user-mgmt-svcs/auth/tenants?'
        user_name_query_params={ 'userName' : user_name}
        tenants_response = requests.get(tenants_url+urllib.parse.urlencode(user_name_query_params))
        
        if tenants_response.status_code != 200:
            print("Failed to get list of instance tenants.")
            return
        
        tenant_list = json.loads(tenants_response.content.decode("utf-8"))
        
        tenant_id = ""
        for t in tenant_list:
            if t["name"] == self.tenant_name:
                tenant_id = t["id"]

        token_url = self.uri + '/user-mgmt-svcs/auth/oauth/devicecode'
        token_request_payload={
            "tenantId" : tenant_id,
            "oauthToken" : oauth_token,
            "userName" : user_name
        }
        token_response = requests.post(token_url, json=token_request_payload)
        access_token = token_response.content.decode()
        self.token = access_token

        profile_url = self.uri + '/user-mgmt-svcs/user/profile'
        profile_response = requests.get(profile_url, headers={'Authorization': 'Bearer '+access_token})
        if profile_response.status_code != 200:
            print("Authentication Failed.")
            return
        print("Authentication Successful.")

########################################
# Basic Config
########################################

    def __get_tenant_solutionid(self):
        uri = self.uri + "/data-svcs/solution"

        response = requests.get(
            uri,
            headers={'Authorization': 'Bearer %s' % self.token},
            json={}
        )
        if response.status_code != 200:
            print(response.status_code)
            print("Failed to get tenant id from Kobai")
            return None
        solutionId = response.json()[0]["id"]
        return str(solutionId)
    
    def __get_tenant_export(self) -> str:

        self.id = self.__get_tenant_solutionid()
        if self.id is None:
            return
        
        uri = self.uri + "/data-svcs/solutions/export/" + self.id

        response = requests.get(
            uri,
            headers={'Authorization': 'Bearer %s' % self.token},
            json={}
        )
        if response.status_code != 200:
            print(response.status_code)
            print("Failed to get tenant config from Kobai")
            return None
        return response.json()
    
    def get_tenant_config(self):
        tenant_export = self.__get_tenant_export()
        tenant_decoded = json.loads(tenant_export)
        for dom in enumerate(tenant_decoded['domains']):
            if dom[1]['concepts'] != None:
                conText = base64.b64decode(dom[1]['concepts']).decode('UTF-8')
                cons = json.loads(conText)
                tenant_decoded['domains'][dom[0]]['concepts'] = cons
        for query in enumerate(tenant_decoded['queries']):
            if query[1]['queryDefinition'] != None:
                qDefText = base64.b64decode(query[1]['queryDefinition']).decode('UTF-8')
                qDef = json.loads(qDefText)
                tenant_decoded['queries'][query[0]]['queryDefinition'] = qDef
                qDefText = base64.b64decode(query[1]['runtimeDefinition']).decode('UTF-8')
                qDef = json.loads(qDefText)
                tenant_decoded['queries'][query[0]]['runtimeDefinition'] = qDef
        for queryC in enumerate(tenant_decoded['queryCalcs']):
            if queryC[1]['expression'] != None:
                qDefText = base64.b64decode(queryC[1]['expression']).decode('UTF-8')
                qDef = qDefText
                tenant_decoded['queryCalcs'][queryC[0]]['expression'] = qDef
                qDefText = base64.b64decode(queryC[1]['argumentDefinition']).decode('UTF-8')
                qDef = json.loads(qDefText)
                tenant_decoded['queryCalcs'][queryC[0]]['argumentDefinition'] = qDef
        for viz in enumerate(tenant_decoded['visualizations']):
            if viz[1]['definition'] != None:
                qDefText = base64.b64decode(viz[1]['definition']).decode('UTF-8')
                qDef = json.loads(qDefText)
                tenant_decoded['visualizations'][viz[0]]['definition'] = qDef
        #TODO: Not decoding data source conn props
        self.tenant_json = tenant_decoded
        return tenant_decoded
    
########################################
# Spark Functions
########################################

    def spark_init_session(self, spark_session: SparkSession):
        
        """
        Initialize a client allowing the SDK to use a Spark Session to execute Spark SQL commands, like creating tables and views.

        Parameters:
        spark_session (SparkSession): Your spark session (eg. of the notebook you are using)
        """

        self.spark_client = spark_client.SparkClient(spark_session)
        #self.id = self.__get_tenant_solutionid()

    def spark_generate_genie_views(self):

        """
        Use the Spark Client to generate views for this tenant required to populate a Genie Data Room.
        """

        tables = self.__get_view_sql()
        for t in tables:
            self.spark_client._SparkClient__run_sql(t["sql"])
        print("Updated " + str(len(tables)) + " views for Genie.")

    def spark_remove_genie_views(self):
        
        """
        Use the Spark Client to remove any views previously created for this tenant.
        """

        tables = self.__get_view_sql()
        for t in tables:
            self.spark_client._SparkClient__run_sql("DROP VIEW " + t["table"])
        print("Removed " + str(len(tables)) + " views.")

########################################
# Databricks Functions
########################################

    def databricks_init_notebook(self,  notebook_context, warehouse_id: str):
        
        """
        Initialize a client allowing the SDK to use a Databricks Notebook context to access configuration parameters required to call Databricks APIs.

        Parameters:
        notebook_context: Your notebook context. Suggestion: dbutils.notebook.entry_point.getDbutils().notebook().getContext()
        warehouse_id (str): Identifier for a Databricks SQL Warehouse. When resources are created that require compute to be configured (eg. Data Rooms), this warehouse will be used. 
        """

        self.databricks_client = databricks_client.DatabricksClient(notebook_context, warehouse_id)

    def databricks_build_genie(self):

        """
        Use the Databricks Client to create a Genie Data Room for this tenant.
        """
        
        data_rooms = self.databricks_client._DatabricksClient__api_get("/api/2.0/data-rooms")
        room_id = "-1"
        if data_rooms:
            for dr in data_rooms["data_rooms"]:
                if dr["display_name"] == self.tenant_name:
                    room_id = dr["id"]
        
        payload = {"display_name":self.tenant_name,"description":"Genie for Kobai tenant " + self.tenant_name,"stage":"DRAFT","table_identifiers":[],"warehouse_id":self.databricks_client.warehouse_id,"run_as_type":"VIEWER"}
        if room_id == "-1":
            response = self.databricks_client._DatabricksClient__api_post("/api/2.0/data-rooms", payload)
            room_id = response["id"]

        for t in self.__get_view_sql():
            payload["table_identifiers"].append(t["table"])
        response = self.databricks_client._DatabricksClient__api_post("/api/2.0/data-rooms/" + room_id, payload)

        payload = {"title":"Notes","content":"When filtering for a named entity, use a like comparison instead of equality.","instruction_type":"TEXT_INSTRUCTION"}
        instructions = self.databricks_client._DatabricksClient__api_get("/api/2.0/data-rooms/" + room_id + "/instructions")
        inst_id = "-1"
        if instructions:
            for i in instructions["instructions"]:
                if i["title"] == "Notes":
                    inst_id = i["id"]

            response = self.databricks_client._DatabricksClient__api_post("/api/2.0/data-rooms/" + room_id + "/instructions/" + inst_id, payload)
        else:
            response = self.databricks_client._DatabricksClient__api_post("/api/2.0/data-rooms/" + room_id + "/instructions", payload)

        print("Done creating your Data Room. You can access it here: https://" + self.databricks_client.workspace_uri + "/data-rooms/rooms/" + room_id)

########################################
# Semantic Profile
########################################

    def __get_descriptions(self):
        uri = self.uri + "/episteme-svcs/descriptions"

        response = requests.get(
            uri,
            params={"schema": self.schema, "tenant_id": self.id},
            headers={'Authorization': 'Bearer %s' % self.token},
            json={}
        )
        if response.status_code != 200:
            print("Failed to get semantic data from Kobai.")
            print(response.status_code)
            return None
        return response.json()
     

    def __get_view_sql(self):
        sql_list = []
        descriptions = self.__get_descriptions()
        for dom in descriptions["domains"]:
            for con in dom["concepts"]:
                con_label = dom["name"] + "_" + con["name"]
                out_table = con["table"].replace(".data_", ".genie_").replace("_np", "")
                sql = "CREATE OR REPLACE VIEW " + out_table + " "
                sql += "(" + con_label + " COMMENT '" + con["id_description"] + "', "
                from_sql = "(SELECT DISTINCT _conceptid, p1 FROM " + con["table"] + ") AS " + dom["name"] + "_" + con["name"] + "_ID "
                as_sql = "SELECT DISTINCT " + con_label + "_ID._conceptid " + con_label + ", "
                as_props = []
                top_props = []
                for prop in con["properties"]:
                    prop_label = con_label + "_" + prop["name"]
                    prop_name = self.id + "/" + prop["uri"].split("/")[-2] + "/" + prop["uri"].split("/")[-1]
                    from_sql += "LEFT JOIN " + con["table"] + " AS " + prop_label + " ON " + prop_label + ".type='l' AND " + prop_label + ".name='" + prop_name + "' AND " + prop_label + ".scenario='' AND " + con_label + "_ID.p1=" + prop_label + ".p1 AND " + con_label + "_ID._conceptid=" + prop_label + "._conceptid "
                    as_props.append(prop_label + ".value " + prop_label)
                    top_props.append(prop_label + " COMMENT '" + prop["sentence"] + "'")
                for prop in con["relations"]:
                    prop_label = con_label + "_" + prop["name"]
                    prop_name = self.id + "/" + prop["uri"].split("/")[-2] + "/" + prop["uri"].split("/")[-1]
                    from_sql += "LEFT JOIN " + con["table"] + " AS " + prop_label + " ON " + prop_label + ".type='r' AND " + prop_label + ".name='" + prop_name + "' AND " + prop_label + ".scenario='' AND " + con_label + "_ID.p1=" + prop_label + ".p1 AND " + con_label + "_ID._conceptid=" + prop_label + "._conceptid "
                    as_props.append(prop_label + ".value " + prop_label)
                    top_props.append(prop_label + " COMMENT '" + prop["sentence"] + "'")
                as_sql += ", ".join(as_props)
                as_sql += " FROM " + from_sql
                sql += ", ".join(top_props) + ") "
                sql += "COMMENT '" + con["description"] + "' "
                sql += "AS " + as_sql
                sql_list.append({"table": out_table, "sql": sql})
        return sql_list


