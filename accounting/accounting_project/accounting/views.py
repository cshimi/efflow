# your_app_name/views.py

from django.shortcuts import render, redirect
from .forms import TransactionCSVUploadForm
from django.conf import settings
import os

def landing_page(request):
    return render(request, 'accounting/landing_page.html')

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
            return render(request, 'accounting/landing_page.html')
    else:
        form = TransactionCSVUploadForm()
    return render(request, 'accounting/upload_csv.html', {'form': form})
