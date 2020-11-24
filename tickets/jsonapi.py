import json
import requests 

headers = {'token': 'a7d9b4b8b8f66da7bf5139389d41eec72ca9f42c1d5832e22c4d4ce174e26aea' }


resp = requests.get('http://smart-api.smartnx.io/api/v1/helpdesk/services?company_id=28&rows=10&page=1',headers=headers)
resp2 = requests.get('https://smart-api.smartnx.io/api/v1/helpdesk/tickets/109340?company_id=28',headers=headers)
class Jason():
    def printResp(self):
       print('a')

#print (resp.json())
