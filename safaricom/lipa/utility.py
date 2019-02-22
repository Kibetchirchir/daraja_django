import requests
from requests.auth import HTTPBasicAuth
import os


class StkPush:
    def stk_request(self,phone, amount, acc):
        access_token = "Access-Token"
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s 4Agx7NGvNFKhDCOKw09ODiPBEQog"}
        request = {
            "BusinessShortCode": " ",
            "Password": " ",
            "Timestamp": " ",
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": os.getenv("PAYBILL"),
            "PhoneNumber": phone,
            "CallBackURL": os.getenv("CALLBACKURL"),
            "AccountReference": acc,
            "TransactionDesc": " "
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

        r = requests.get(api_url, auth=HTTPBasicAuth(consumer_key, consumer_secret))

        return r


class Password:
    def password(self):
        pass
