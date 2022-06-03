import json
import argparse
import hashlib

def main(args):
    # ap = argparse.ArgumentParser()
    # ap.add_argument("--RFID", required=True, default=None, type=str,)
    # args = vars(ap.parse_args(args))
    RFID = str(args).encode('utf-8')
    data = []

    with open('MOCK_DATA.json', 'r') as f:
        f.seek(0)
        data = json.load(f)
        if hashlib.md5(RFID).hexdigest() in data:
            return True
        else:
            return False