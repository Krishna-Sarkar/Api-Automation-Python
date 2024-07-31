import json
from lib.utils.DataReader import read_json
from lib.utils.Request_Executor import Send_Request



def createToken(check_server):
    config=check_server
    url = config['integration']['url']+config['integration']['createTokenUri']
    payload = read_json('request_createtoken_body.json')
    headers = read_json('request_createtoken_header.json')
    response=Send_Request().send("POST", url, data=json.dumps(payload),headers=headers)
    return json.loads(response.text)['token']