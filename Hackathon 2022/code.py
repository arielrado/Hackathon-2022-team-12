from urllib import response
import requests
import re
import serial,time

port = 'COM8'
try:
    print ("Trying...",port)
    arduino = serial.Serial(port,9600)
except:
    print("failed to connect on",port)
while 1:
    time.sleep(1)
    x = str(arduino.readline())
    edit = "".join(re.findall("[A-Z0-9]",x))
    print(edit)
    respo = requests.get('http://10.176.94.30:9000/'+edit)
    if respo.status_code == 200:
        print('SUCCESS')
        
    else:
        print('FAIL')