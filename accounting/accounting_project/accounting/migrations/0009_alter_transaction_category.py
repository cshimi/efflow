# Generated by Django 4.2.5 on 2023-10-12 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0008_remove_transaction_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.CharField(max_length=100),
        ),
    ]
