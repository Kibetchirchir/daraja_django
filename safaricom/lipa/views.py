from rest_framework import generics, request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Transaction
from .serialiser import TransactionSerializer
from rest_framework.decorators import api_view


class LipaMpesa(APIView):
    def get(self, request, format=None):
        queryset = Transaction.objects.all()
        serializer_class = TransactionSerializer
        return Response(serializer_class.data)

    def post(self, request, format=None):
        request.data["name"] = "Kelvin Chirchir"
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED,)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


