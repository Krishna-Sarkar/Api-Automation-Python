import requests
from lib.common.Create_token import createToken
from lib.utils.DataReader import read_json
from lib.utils.Request_Executor import Send_Request
import json

def test_validate_CreateToken(check_server):
    config=check_server
    url = config['integration']['url']+config['integration']['createTokenUri']
    payload = read_json('request_createtoken_body.json')
    headers = read_json('request_createtoken_header.json')
    response=Send_Request().send("POST", url, data=json.dumps(payload),headers=headers)
    assert json.loads(response.text)['token'] != None
    
def test_validate_CreateDelete(check_server):
    config=check_server
    url = config['integration']['url']+config['integration']['createUri']
    payload = read_json('request_createBooking_body.json')
    headers = read_json('request_createtoken_header.json')
    response=Send_Request().send("POST", url, data=json.dumps(payload),headers=headers)
    assert json.loads(response.text)['bookingid'] != None
    booking_id=json.loads(response.text)['bookingid']
    url = url+'/'+str(booking_id)
    response=Send_Request().send("GET", url)
    assert json.loads(response.text)['firstname']=='krishna'
    assert json.loads(response.text)['bookingdates']['checkout']=='2024-01-02'
    headers = read_json('request_deleteBooking_header.json')
    response=Send_Request().send("DELETE", url,headers=headers,status=201)    

def test_validate_update(check_server):
    config=check_server
    token_id=createToken(check_server)
    url = config['integration']['url']+config['integration']['createUri']
    payload = read_json('request_createBooking_body.json')
    headers = read_json('request_createtoken_header.json')
    response=Send_Request().send("POST", url, data=json.dumps(payload),headers=headers)
    assert json.loads(response.text)['bookingid'] != None
    booking_id=json.loads(response.text)['bookingid']
    url = url+'/'+str(booking_id)
    headers = read_json('request_updatebooking_header.json')
    headers['Cookie']='token='+token_id
    payload = read_json('request_updatebooking_body.json')
    response=Send_Request().send("PATCH", url, data=json.dumps(payload),headers=headers)
    assert json.loads(response.text)['firstname'] == 'krishna1'
    response=Send_Request().send("DELETE", url,headers=headers,status=201)