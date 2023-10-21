# your_app_name/views.py

import os, csv
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, Http404  # Add this import
from .forms import TransactionCSVUploadForm
from .models import TransactionCSV, Account, Category, Transaction
from datetime import datetime

def landing_page(request):
    # Query the database to retrieve a list of uploaded files
    uploaded_files = TransactionCSV.objects.all()
    context = {
        'uploaded_files': uploaded_files,
    }
    return render(request, 'accounting/landing_page.html', context)

def upload_csv(request):
    csv_files_directory = os.path.join(settings.MEDIA_ROOT, 'transaction_csv_files')
    if request.method == 'POST':
        form = TransactionCSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            file_list = os.listdir(csv_files_directory)
            if uploaded_file.name not in file_list:
                form.save()
                return redirect('landing_page')
            else:
                # Handle file already exists error
                form.add_error('file', 'A file with this name already exists.')
    else:
        form = TransactionCSVUploadForm()
    return render(request, 'accounting/upload_csv.html', {'form': form})


def read_csv_file(file_path):
    data = []
    with open(file_path, mode='r', encoding='utf-8-sig') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')
        data = list(csv_reader)

    summary = {}
    for row in data[:4]:
        key, value = row[0], row[1]
        key = key.strip('"').strip(':').replace(' ', '_')
        summary[key] = value.strip('"').strip('="')

    data = data[8:-3]
    # Process and save data to the Transaction database
    for row in data:
        date = datetime.strptime(row[0], '%d.%m.%Y').strftime('%Y-%m-%d')  # Format the date
        type_of_transaction = row[1]
        # notification_text = row[2]
        credit_in_chf = row[3]
        debit_in_chf = row[4]

        # You may need to map these fields to match your Transaction model

        # Find or create the Account and Category
        account_name = summary['Account']
        category_name = type_of_transaction

        account, _ = Account.objects.get_or_create(name=account_name)
        category, _ = Category.objects.get_or_create(name=category_name)

        # Create and save the Transaction
        transaction = Transaction(
            date=date,
            description=type_of_transaction,
            amount=credit_in_chf or debit_in_chf,  # Use either credit or debit amount
            account=account,
            category=category,
        )
        transaction.save()
    return summary, data


def print_data(request, file_id):
    try:
        transaction_csv = TransactionCSV.objects.get(id=file_id)
        file_path = transaction_csv.file.path

        # Read and process the data from the CSV file
        summary, data = read_csv_file(file_path)

        # Create a list of dictionaries for each transaction
        transactions = []
        for row in data:
            date, type_of_transaction, notification_text, credit_in_chf, debit_in_chf = row
            transactions.append({
                'date': date,
                'type_of_transaction': type_of_transaction,
                'notification_text': notification_text,
                'credit_in_chf': credit_in_chf,
                'debit_in_chf': debit_in_chf,
            })

        # Render the print_data.html template with the context data
        context = {
            'summary': summary,
            'transactions': transactions,  # Pass the list of transactions
        }
        return render(request, 'accounting/print_data.html', context)

    except TransactionCSV.DoesNotExist:
        raise Http404("File not found.")