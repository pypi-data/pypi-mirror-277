import json
import API
from API import Common


def create_file(ws_config, device_serial, filename, file_size, sha256_hash):

    try:
        json_post_data = {"deviceSerial":device_serial, "filename":filename, "fileSize":file_size, "sHA256Hash":sha256_hash}

        method = "POST"
        path = 'v1/file'
        url = ws_config.base_url + path
        headers = {"Content-Type": "application/json"}
        parameters = ''
        body = json.dumps(json_post_data)

        response_code, response_string = API.Common.send_signed_request(ws_config, method, url, path, headers, parameters, body)

        signed_url = ''
        file_id = 0
        
        if (response_code == 200):

            # This response should include signedURL, fileID
            response_data = json.loads(response_string)

            signed_url = response_data['signedURL']
            file_id = response_data['fileID']

    except Exception as ex:
        
        filename, line_number = Common.get_exception_info()

        if filename is not None and line_number is not None:
            print(f"Exception occurred at line {line_number} in {filename}")
        print(ex)

        response_code = -1
        response_string = "Exception in create_file"
        signed_url = ""
        file_id = 0

    return response_code, response_string, signed_url, file_id


def update_file_upload_success(ws_config, device_name, file_id):

    try:
        json_post_data = {'deviceSerial':device_name}

        method = "POST"
        path = 'v1/file/success/' + str(file_id)
        url = ws_config.base_url + path
        headers = {"Content-Type": "application/json"}
        parameters = ''
        body = json.dumps(json_post_data)

        response_code, response_string = Common.send_signed_request(ws_config, method, url, path, headers, parameters, body)

    except Exception as ex:
        
        filename, line_number = Common.get_exception_info()
        if filename is not None and line_number is not None:
            print(f"Exception occurred at line {line_number} in {filename}")
        print(ex)

        response_code = -1
        response_string = "Exception in update_file_upload_success"

    return response_code, response_string

