python manage.py makemigrations
python manage.py migrate

# Start the Django development server
python manage.py runserver

. /Users/christianashimitra/anaconda3/bin/activate && conda activate /Users/christianashimitra/anaconda3/envs/MachineLearningTraining;




def upload_file(request):
    # Get a list of existing files in the media uploads folder
    existing_files = os.listdir('media/uploads')  # Replace 'media/uploads' with your actual media directory path

    if request.method == 'POST':
        uploaded_file = request.FILES['csv_file']
        if uploaded_file.name.endswith('.csv'):
            # Check if the file with the same name exists in existing_files list
            if uploaded_file.name in existing_files:
                # File with the same name already exists, handle this case as needed
                # You can redirect the user to an error page or display a message
                return render(request, 'analysis/file_already_exists.html')

            # Save the uploaded file
            file_instance = UploadedFile(file=uploaded_file)
            file_instance.save()

            # Read and process the CSV file
            with open(file_instance.file.path, mode='r', encoding='utf-8-sig') as csvfile:
                csv_reader = csv.reader(csvfile)
                data = list(csv_reader)

            # Extract summary information
            summary = {}
            for row in data[:5]:
                key, value = row[0].split(';=')
                key = key.strip().replace(':', '')
                summary[key.strip()] = value.strip().strip('"')

            # Remove the first 6 rows (summary) and keep the rest for the table
            data = data[6:]

            return render(request, 'analysis/display_csv.html', {'data': data, 'summary': summary, 'existing_files': existing_files})

    return render(request, 'analysis/upload.html', {'existing_files': existing_files})



def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['csv_file']
        if uploaded_file.name.endswith('.csv'):
            # Define the storage path
            storage_path = os.path.join('media', 'uploads', uploaded_file.name)
            file_instance = UploadedFile(file=uploaded_file)

            # Check if the file with the same name exists
            if not os.path.exists(storage_path):
                # Save the uploaded file if it doesn't exist
                file_instance.save()
            else:
                # File with the same name already exists, handle this case as needed
                return render(request, 'analysis/file_already_exists.html')

            return render(request, 'analysis/file_uploaded.html', {'file_instance': file_instance})

    return render(request, 'analysis/upload.html')

def display_file(request, file_id):
    try:
        # Retrieve the UploadedFile instance by its ID
        file_instance = UploadedFile.objects.get(pk=file_id)

        # Read and process the CSV file
        with open(file_instance.file.path, mode='r', encoding='utf-8-sig') as csvfile:
            csv_reader = csv.reader(csvfile)
            data = list(csv_reader)

        # Extract summary information
        summary = {}
        for row in data[:5]:
            key, value = row[0].split(';=')
            key = key.strip().replace(':', '')
            summary[key.strip()] = value.strip().strip('"')

        # Remove the first 6 rows (summary) and keep the rest for the table
        data = data[6:]

        return render(request, 'analysis/display_csv.html', {'data': data, 'summary': summary, 'file_instance': file_instance})
    except UploadedFile.DoesNotExist:
        # Handle the case where the file with the specified ID doesn't exist
        return render(request, 'analysis/file_not_found.html')
import os
from django.shortcuts import render, redirect
from .models import UploadedFile
import csv
from django.shortcuts import render

def landing_page(request):
    # Get a list of existing CSV files in the media/uploads folder
    existing_files = [file for file in os.listdir('media/uploads') if file.endswith('.csv')]
    print(1)
    print('sdsda')
    print('sdsda')
    print('sdsda')
    print('sdsda')
    return render(request, 'analysis/landing_page.html', {'existing_files': existing_files})


def upload_file(request):
    print(2)
    print('sdsda')
    print('sdsda')
    print('sdsda')
    print('sdsda')
    # Get a list of existing files in the media uploads folder
    existing_files = os.listdir('media/uploads')  # Replace 'media/uploads' with your actual media directory path
    print('few')

    if request.method == 'POST':
        # Get the uploaded file from the form
        uploaded_file = request.FILES.get('csv_file', None)
        if uploaded_file:
            if uploaded_file.name.endswith('.csv'):
                # Define the storage path for the uploaded file
                storage_path = os.path.join('media', 'uploads', uploaded_file.name)

                # Check if a file with the same name already exists
                if not os.path.exists(storage_path):
                    # Save the uploaded file if it doesn't exist
                    file_instance = UploadedFile(file=uploaded_file)
                    file_instance.save()
                else:
                    # File with the same name already exists, handle this case as needed
                    return render(request, 'analysis/file_already_exists.html')
        # Render the upload.html template for GET requests or unsuccessful uploads
        return render(request, 'analysis/landing_page.html', {'existing_files': existing_files})

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
        return render(request, 'analysis/file_not_found.html')


from django.urls import path
from . import views

urlpatterns = [
    # URL for the landing page (where users can choose to upload a file or select an existing one)
    path('', views.landing_page, name='landing_page'),

    # URL for uploading a new file
    path('upload/', views.upload_file, name='upload_file'),

    # URL for displaying an existing file's details
    path('display/<int:file_id>/', views.display_file, name='display_file'),

    # Add more URL patterns for other views as needed
    # For example, if you have a "print_file" view, you can add a URL pattern for it here.
]
