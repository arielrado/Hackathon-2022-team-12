from urllib import response
import requests

respo = requests.get('http://10.176.94.30:9000/035D5D11')

if respo.status_code == 200:
    print('SUCCESS')
else:
    print('FAIL')