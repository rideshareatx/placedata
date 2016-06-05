import os
import requests

root_dir = os.path.dirname(os.path.realpath(__file__))

server_url = 'http://localhost:8080'

auth = {'grant_type': 'password', 'username': 'test', 'password': 'password'}

token = requests.post(server_url+'/management/token', data=auth).json()

org = 'test-organization'
app = "newapp"
url = server_url+'/{}/{}/place?access_token={}'.format(org, app, token['access_token'])

with open(os.path.join(root_dir, 'buildings.txt')) as f:
    for line in f:
        r = requests.put(url, data=line)