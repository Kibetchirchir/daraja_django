from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Transaction
from .serialiser import TransactionSerializer
from .utility import StkPush, Auth
import json
import datetime


class LipaMpesa(APIView):
    def get(self, request, format=None):
        queryset = Transaction.objects.all()
        serializer_class = TransactionSerializer
        return Response(serializer_class.data)

    def post(self, request, format=None):
        request.data["name"] = "Kelvin Chirchir"
        phone = request.data["phone_number"]
        amount = request.data["amount"]
        acc_reference = request.data["acc_reference"]
        push = StkPush()
        push_result=push.stk_request(phone, amount, acc_reference)
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED,)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


