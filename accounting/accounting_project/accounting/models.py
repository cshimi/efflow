# accounting/models.py - This file defines the database models for the accounting application.

from django.db import models

# Each model class corresponds to a database table.
# Fields in the model represent columns in the database table.

# Account model: Represents accounts with a name and balance.
class Account(models.Model):
    name = models.CharField(max_length=100)  # Field for the account name
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Field for the account balance with a default value

# Category model: Represents categories with a name.
class Category(models.Model):
    name = models.CharField(max_length=100)  # Field for the category name

# Transaction model: Represents individual transactions with date, description, amount, and related account and category.
class Transaction(models.Model):
    date = models.DateField()  # Field for the transaction date
    description = models.CharField(max_length=200)  # Field for the transaction description
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Field for the transaction amount
    account = models.ForeignKey(Account, on_delete=models.CASCADE)  # Relationship to the Account model
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Relationship to the Category model

# TransactionCSV model: Represents uploaded CSV files with related data and upload timestamp.
class TransactionCSV(models.Model):
    file = models.FileField(upload_to='transaction_csv_files/')  # Field for the uploaded CSV file
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Field for the timestamp when the file was uploaded

    def __str__(self):
        return self.file.name  # A custom string representation for the model instance

# Data validation rules and constraints are specified in the models,
# and these rules are enforced at the database level.

# Models are used to create, retrieve, update, and delete records in the database.