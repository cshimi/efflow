# Generated by Django 4.2.5 on 2023-10-09 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0002_transactioncsv_delete_bankstatementupload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactioncsv',
            name='date_from',
        ),
        migrations.RemoveField(
            model_name='transactioncsv',
            name='date_to',
        ),
    ]
