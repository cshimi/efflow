# Generated by Django 4.2.5 on 2023-10-12 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0010_account_new_fiscalyear_transaction_new_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iban', models.CharField(max_length=30)),
                ('currency', models.CharField(max_length=10)),
            ],
        ),
    ]
