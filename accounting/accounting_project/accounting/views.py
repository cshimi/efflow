# your_app_name/views.py

import os, csv, datetime
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse  # Add this import
from .forms import TransactionCSVUploadForm
from .models import TransactionCSV



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
            # Check if the uploaded file already exists in the directory
            if uploaded_file.name not in file_list:
                form.save()
                # File does not exist, save it
            return redirect('landing_page')
    else:
        form = TransactionCSVUploadForm()
    return render(request, 'accounting/upload_csv.html', {'form': form})

def print_data(request):
    if request.method == 'POST':
        file_id = request.POST.get('file_id')
        try:
            transaction_csv = TransactionCSV.objects.get(id=file_id)
            file_path = transaction_csv.file.path

            # Read and print the data from the CSV file
            data = read_csv_file(file_path)

            # You can customize how you want to display the data, e.g., in an HTML template
            # Here, we simply convert it to a string and display it in an HttpResponse
            data_str = "\n".join([str(entry) for entry in data])

            return HttpResponse(data_str, content_type='text/plain')
        except TransactionCSV.DoesNotExist:
            return HttpResponse("File not found.", content_type='text/plain')

    # Handle GET request or invalid form submission
    return redirect('landing_page')

def read_csv_file(file_path):
    data = []

    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter='\t')

        for row in csvreader:
            entry = {
                'Date': row['Date'],
                'Type of transaction': row['Type of transaction'],
                'Notification text': row['Notification text'],
                'Credit in CHF': row['Credit in CHF'],
                'Debit in CHF': row['Debit in CHF'],
            }
            data.append(entry)

    return data
