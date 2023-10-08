import os
from django.shortcuts import render, redirect
from .models import UploadedFile
import csv

def get_existing_files():
    media_folder = 'media/uploads'  # Replace with your actual media directory path
    existing_files = []

    if os.path.exists(media_folder):
        existing_files = [file for file in os.listdir(media_folder) if file.endswith('.csv')]

    return existing_files

def upload_file(request):
    existing_files = get_existing_files()

    if request.method == 'POST':
        selected_file = request.POST.get('existing_file')  # Get the selected existing file
        uploaded_file = request.FILES.get('csv_file', None)

        if selected_file:
            # Redirect to display the selected existing file
            return redirect('display_file', file_id=selected_file)
        elif uploaded_file:
            if uploaded_file.name.endswith('.csv'):
                # Check if the file with the same name exists
                if uploaded_file.name not in existing_files:
                    # Save the uploaded file if it doesn't exist
                    storage_path = os.path.join('media', 'uploads', uploaded_file.name)
                    file_instance = UploadedFile(file=uploaded_file)
                    file_instance.save()
                else:
                    # File with the same name already exists, handle this case as needed
                    return render(request, 'analysis/file_already_exists.html')

                return redirect('display_file', file_id=file_instance.pk)

    return render(request, 'analysis/upload.html', {'existing_files': existing_files})
from django.shortcuts import render
from .models import UploadedFile
import csv
from django.http import Http404

def display_file(request, file_id):
    try:
        # Retrieve the UploadedFile instance by its ID
        file_instance = UploadedFile.objects.get(pk=file_id)

        # Read and process the CSV file
        with open(file_instance.file.path, mode='r', encoding='utf-8-sig') as csvfile:
            csv_reader = csv.reader(csvfile)
            data = list(csv_reader)

        # Extract summary information from the first 5 rows
        summary = {}
        for row in data[:5]:
            key, value = row[0].split(';=')  # Split the key and value using the ';=' separator
            key = key.strip().replace(':', '')  # Remove ':' and leading/trailing spaces
            summary[key.strip()] = value.strip().strip('"')  # Remove surrounding double quotes

        # Remove the first 6 rows (summary) and keep the rest for the table
        data = data[6:]

        # Render the display_csv.html template with data and summary
        return render(request, 'analysis/display_csv.html', {'data': data, 'summary': summary, 'file_instance': file_instance})
    except UploadedFile.DoesNotExist:
        # Handle the case where the file with the specified ID doesn't exist
        raise Http404("File does not exist")
