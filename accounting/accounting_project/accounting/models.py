# accounting/models.py

from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

class Category(models.Model):
    name = models.CharField(max_length=100)

class Transaction(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class TransactionCSV(models.Model):
    file = models.FileField(upload_to='transaction_csv_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    #date_from = models.DateField()
    #date_to = models.DateField()

    def __str__(self):
        return self.file.name