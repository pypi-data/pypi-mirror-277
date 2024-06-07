import datetime
import json
from json import JSONEncoder

import ActionStreamerWS
from ActionStreamerWS import CommonFunctions

class WebServiceConfig:

    def __init__(self, access_key, secret_key, base_url, timeout=30, ignore_ssl=False):
        self.access_key = access_key
        self.secret_key = secret_key
        self.base_url = base_url
        self.timeout = timeout
        self.ignore_ssl = ignore_ssl

class LogConfig:

    def __init__(self, ws_config, device_name, agent_type, agent_version, agent_index, process_id):
        self.ws_config = ws_config
        self.device_name = device_name
        self.agent_type = agent_type
        self.agent_version = agent_version
        self.agent_index = agent_index
        self.process_id = process_id

class PatchOperation:

    def __init__(self, field_name, value):
        self.field_name = field_name
        self.value = value
        
class WebServiceResult:

    def __init__(self, code, description, http_response_code, http_response_string, json_data):
        self.Code = code
        self.Description = description
        self.HttpResponseCode = http_response_code
        self.HttpResponseString = http_response_string
        self.JsonData = json_data

class DateTimeEncoder(JSONEncoder):

    # Override the default method
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()


def register_agent(ws_config, device_name, agent_type, agent_version, agent_index, process_id):

    try:        
        jsonPostData = {"deviceName":device_name, "agentType":agent_type, "agentVersion":agent_version, "agentIndex":agent_index, "processID":process_id}

        method = "POST"
        path = 'v1/agent'
        url = ws_config.base_url + path
        headers = {"Content-Type": "application/json"}
        parameters = ''
        body = json.dumps(jsonPostData)
        
        response_code, response_string = CommonFunctions.send_signed_request(ws_config, method, url, path, headers, parameters, body)

    except Exception as ex:
        
        filename, line_number = CommonFunctions.get_exception_info()
        if filename is not None and line_number is not None:
            print(f"Exception occurred at line {line_number} in {filename}")
        print(ex)

        response_code = -1
        response_string = "Exception in RegisterAgent"

    return response_code, response_string
