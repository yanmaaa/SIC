import time
import requests

TOKEN = "BBFF-VwPygnvrOxguX7DWtpy6eJDTNDTzYY"  # Put your TOKEN here
DEVICE_LABEL = "sic"  # Put your device label here 
VARIABLE_LABEL_1 = "sensor_depan"  # Put your first variable label here
VARIABLE_LABEL_2 = "sensor_kanan"  # Put your second variable label here
VARIABLE_LABEL_3 = "sensor_kiri"  # Put your second variable label here
VARIABLE_LABEL_4 = "latitude"
VARIABLE_LABEL_5 = "longitude"
# VARIABLE_LABEL_6 = "decision"

def build_payload(value_1, value_2, value_3, value_4, value_5):
   
    payload = {VARIABLE_LABEL_1: value_1,
              VARIABLE_LABEL_2: value_2,
              VARIABLE_LABEL_3: value_3,
              VARIABLE_LABEL_4: value_4,
              VARIABLE_LABEL_5: value_5}
            #   VARIABLE_LABEL_6: value_6}
    return payload

def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)

    # Processes results
    print(req.status_code, req.json())
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True


def main():
    payload = build_payload(
        VARIABLE_LABEL_1, VARIABLE_LABEL_2, VARIABLE_LABEL_3)

    print("[INFO] Attemping to send data")
    post_request(payload)
    print("[INFO] finished")
