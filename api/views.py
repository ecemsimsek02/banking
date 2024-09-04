from __future__ import unicode_literals

from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.shortcuts import render
from django.http import Http404
from django.views import View
from rest_framework import generics,status
from rest_framework.response import Response 
from rest_framework.views import APIView

from .models import *
from .serializers import *
from django.http import HttpResponse 
import logging
import django_filters
import json

class BranchesAPIView(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class BranchDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class BanksAPIView(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class BankDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class CreateAccountAPIView(APIView):

    def post(self,request):
       
        client = Client.objects.get(pk=request.data['client'])
        bank = Bank.objects.get(pk=request.data['bank'])
        account = Account.objects.create(
            client = client,
            open_date = request.data['open_date'],
            account_type = request.data['account_type'],
            balance=request.data['balance'],
            bank = bank
        )

        serializer = AccountSerializer(account)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

class AccountListAPIView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
class ClientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class BranchesFilterList(ListAPIView):
    serializer_class = BranchSerializer
    filter_backends = [OrderingFilter] 

    def get_queryset(self):
        queryset = Branch.objects.all()
        address = self.request.query_params.get('address')
        if address:
            queryset = queryset.filter(address__icontains=address)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({"detail": "No branches found matching the criteria."}, status=status.HTTP_404_NOT_FOUND)


"""class AccountBalanceViewSet(generics.ListCreateAPIView):
    def retrieve(self, request, pk=None):
        try:
            account = Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            return Response({"error": "Account not found"}, status=404)
        
        serializer= AccountSerializer(Account)
        return Response(serializer.data)"""

class WithdrawViewSet(generics.ListCreateAPIView):
    queryset = Withdraw.objects.all()
    serializer_class = WithdrawSerializer
  
    def post(self, request):
        # Client ve Account'ı almak
        client = Client.objects.get(pk=request.data['client'])
        account = Account.objects.get(pk=request.data['account'])

        # Para yatırma işlemini yapmak
        withdraw_amount = float(request.data['amount'])

        current_balance = float(account.balance)

        new_balance = current_balance - withdraw_amount

        account.balance = new_balance
        account.save()

        withdraw = Withdraw.objects.create(
            amount=withdraw_amount,
            account=account,
            client=client
        )
        log_data = {
                'client_id': client.id,
                'account_id': account.id,
                'amount': withdraw_amount,
                'new_balance': new_balance
        }
        logger.info(f'Withdraw made: {json.dumps(log_data)}')

        # Deposit verisini döndür
        serializer = WithdrawSerializer(withdraw)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
class DepositViewSet(APIView):
 
    def post(self, request):
        
        client = Client.objects.get(pk=request.data['client'])
        account = Account.objects.get(pk=request.data['account'])

        # Para yatırma işlemini yapmak
        deposit_amount = float(request.data['amount'])

        current_balance = float(account.balance)

        new_balance = current_balance + deposit_amount

        account.balance = new_balance
        account.save()

        deposit = Deposit.objects.create(
            amount=deposit_amount,
            account=account,
            client=client
        )
        log_data = {
                'client_id': client.id,
                'account_id': account.id,
                'amount': deposit_amount,
                'new_balance': new_balance
        }
        logger.info(f'Deposit made: {json.dumps(log_data)}')


        # Deposit verisini döndür
        serializer = DepositSerializer(deposit)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
class ClientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['address']

logger = logging.getLogger('bank')

class LogView(APIView):
    def get(self, request, *args, **kwargs):
        # Log mesajını yazdırır
        logger.debug("This is a debug message.")
        return HttpResponse("Log dosyasına yazıldı.")