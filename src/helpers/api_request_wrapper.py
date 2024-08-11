#This will help to make GET,POST,PUT,PATCH Request
import json
import requests


def get_request(url,header):
    get_response = requests.get(url=url,headers=header)
    return get_response

def post_request(url,header,payload,auth,in_json):
    post_response = requests.post(url=url,headers=header,json=payload,auth=auth)
    if in_json is True:
        return post_response.json()
    return post_response



def put_request(url,auth,header,payload,in_json):
    put_response = requests.put(url=url,auth=auth,headers=header,json=payload)
    if in_json is True:
        return put_response.json()
    return put_response

def patch_request(url,auth,header,payload,in_json):
    patch_response = requests.patch(url=url,auth=auth,headers=header,json=payload)
    if in_json is True:
        return patch_response.json()
    return patch_response

def delete_requests(url, headers, auth, in_json):
    delete_response_data = requests.delete(url=url, headers=headers, auth=auth)
    if in_json is True:
        return delete_response_data.json()
    return delete_response_data
