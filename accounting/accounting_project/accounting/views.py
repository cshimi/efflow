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

            # Convert the data to a string with proper encoding (UTF-8)
            data_str = "\n".join([str(entry) for entry in data])

            # Create an HTTP response with UTF-8 encoding
            response = HttpResponse(data_str, content_type='text/plain; charset=utf-8')

            # Set the Content-Disposition header to suggest a file name
            #response['Content-Disposition'] = f'attachment; filename="{transaction_csv.file.name}"'

            return response
        except TransactionCSV.DoesNotExist:
            return HttpResponse("File not found.", content_type='text/plain')

    # Handle GET request or invalid form submission
    return redirect('landing_page')

def read_csv_file(file_path):
    data = []
    with open(file_path, mode='r', encoding='utf-8-sig') as csvfile:
        csv_reader = csv.reader(csvfile)
        data = list(csv_reader)

    summary = {}
    for row in data[:5]:
        key, value = row[0].split(';=')
        key = key.strip().replace(':', '')
        summary[key.strip()] = value.strip().strip('"')

    data = data[6:]

    return summary, data