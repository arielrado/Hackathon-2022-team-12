import json
import argparse
import hashlib


ap = argparse.ArgumentParser()
ap.add_argument("--RFID", required=True, default=None, type=str)
ap.add_argument("--street", required=True, default=None, type=str)
args = vars(ap.parse_args())
data = []
with open('MOCK_DATA.json', 'r') as f:
    f.seek(0)
    data = json.load(f)
    ID = len(data)
    data[hashlib.md5(str(args['RFID']).encode('utf-8')).hexdigest()] = {
        'id' : ID,
        'street' : args['street'],
        'rfid' : args['RFID']
    }
    print(data)

with open('MOCK_DATA.json', 'w') as f:
    f.seek(0)
    json.dump(data, f)
