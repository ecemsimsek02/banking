from rest_framework import serializers 

from .models import * 



class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('name','address','branch_code',)
        read_only_fields = ('id',)

class BranchDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch()
        fields = ('__all__')


class BankSerializer(serializers.ModelSerializer):
    branch = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all()) 
    
    class Meta:
        model = Bank 
        depth=1
        fields = ('__all__')


class ClientManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientManager
        fields = ('__all__')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('__all__')


class AccountSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    bank = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all())
    class Meta:
        model = Account
        fields = ('__all__')



class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ('__all__')


class WithdrawSerializer(serializers.ModelSerializer):
    account = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all())
    client = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all())
    class Meta:
        model = Withdraw
        fields = ('__all__')


class DepositSerializer(serializers.ModelSerializer):
    account = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all())
    client = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all())
    class Meta:
        model = Deposit
        fields = ('__all__')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['name', 'address']