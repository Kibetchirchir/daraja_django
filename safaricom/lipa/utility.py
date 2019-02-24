import requests
from requests.auth import HTTPBasicAuth
import os
import json
import datetime
import base64


class StkPush:
    def stk_request(self,phone, amount, acc):
        access_initialise = Auth()
        access_token_req = access_initialise.auth()
        access_token_json = json.loads(access_token_req)
        access_token = access_token_json["access_token"]
        password = access_initialise.password()
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": os.getenv("short_code"),
            "Password": password,
            "Timestamp": datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": os.getenv("PAYBILL"),
            "PhoneNumber": phone,
            "CallBackURL": os.getenv("CALLBACKURL"),
            "AccountReference": acc,
            "TransactionDesc": "Test"
        }

        response = requests.post(api_url, json=request, headers=headers)

        return response.text


class Auth:
    def __init__(self):
        pass

    def auth(self):
        consumer_key = os.getenv("consumer_key")
        consumer_secret = os.getenv("consumer_secret")
        api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
        request = requests.get(api_url, auth=HTTPBasicAuth(consumer_key, consumer_secret))

        access_token = request.text
        return access_token

    def password(self):
        time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        password_fields = os.getenv("short_code") + os.getenv("pass_key") + time
        password_encode = password_fields.encode("UTF-8")
        password = base64.b64encode(password_encode)
        return str(password)
