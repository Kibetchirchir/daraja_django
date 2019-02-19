import requests
from requests.auth import HTTPBasicAuth
import os
from rest_framework import generics, request
from .models import Transaction
from .serialiser import TransactionSerializer


class Auth:
    def __init__(self):
        pass

    def auth(self):
        consumer_key = os.getenv("consumer_key")
        consumer_secret = os.getenv("consumer_secret")
        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

        return r


class LipaMpesa(generics.ListCreateAPIView):
    print(request)
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
