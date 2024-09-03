from __future__ import unicode_literals
import json
from django.db import models
import logging
logger = logging.getLogger('bank')

class Branch(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    branch_code = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "Branches"



    def json_object(self):
        return {
            "name":self.name,
            "address":self.address,
            "branch_code":self.branch_code
        }
    
    def __str__(self):
        return self.name

class Bank(models.Model):
    name = models.CharField(max_length=250)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)


    def json_object(self):
        return {
            "name": self.name,
            "branch": self.branch
        }

    def __str__(self):
        return self.name 

class ClientManager(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

    def json_object(self):
        return {
            "name":self.name,
            "address":self.address
        }


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk:  # Eğer mevcut bir kayıt güncelleniyorsa
            old_client = Client.objects.get(pk=self.pk)
            if old_client.name != self.name or old_client.address != self.address:
                log_data = {
                    'event': 'Client updated',
                    'client_id': self.pk,
                    'old_name': old_client.name,
                    'new_name': self.name,
                    'old_address': old_client.address,
                    'new_address': self.address
                }
                logger.info(json.dumps(log_data))
        else:  # Yeni bir kayıt ekleniyorsa
            log_data = {
                'event': 'Client created',
                'client_id': self.pk,
                'name': self.name,
                'address': self.address
            }
        logger.info(json.dumps(log_data))
        
        super().save(*args, **kwargs)


class Account(models.Model):
    """Represents Bank Account"""
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    open_date = models.CharField(max_length=250)
    account_type = models.CharField(max_length=250)
    balance = models.FloatField(default=0.0)
    bank = models.ForeignKey(Bank,on_delete=models.CASCADE)


    def json_object(self):
        return {
            
            "open_date":self.open_date,
            "account_type":self.account_type,
            "balance":self.balance,
            "bank":self.bank

        }

    def __str__(self):
        return self.account_type


class Transfer(models.Model):
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)

    def json_object(self):
        return {
            "account":self.account,
            "branch":self.branch
        }

    def __str__(self):
        return "Account Transfered to {} Branch".format(self.branch.name)


class Withdraw(models.Model):
    amount = models.FloatField()
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    client = models.ForeignKey(Client,on_delete=models.CASCADE,default=1,null=True,blank=True)

class Deposit(models.Model):
    amount = models.FloatField()
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    client = models.ForeignKey(Client,on_delete=models.CASCADE,default=1,null=True,blank=True)