from django.shortcuts import render
from .models import UploadedFile
import csv

def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['csv_file']
        if uploaded_file.name.endswith('.csv'):
            # Save the uploaded file
            file_instance = UploadedFile(file=uploaded_file)
            file_instance.save()

            # Read and process the CSV file
            with open(file_instance.file.path, mode='r', encoding='utf-8-sig') as csvfile:
                csv_reader = csv.reader(csvfile)
                data = list(csv_reader)

            #'print(data)
            # Extract summary information
            summary = {}
            for row in data[:5]:
                key, value = row[0].split(';=')
                key = key.strip().replace(':', '')
                summary[key.strip()] = value.strip().strip('"')

            #print(summary)
            #{'Date from': '04.10.2021', 'Date to': '04.10.2023', 'Entry type': 'All',
             #'Account': 'CH5709000000158028028', 'Currency': 'CHF'}

            #for key, value in summary.items():
            #    print(f"Key: {key}, Value: {value}")

            # Remove the first 6 rows (summary) and keep the rest for the table
            data = data[6:]

            return render(request, 'analysis/display_csv.html', {'data': data, 'summary': summary})

    return render(request, 'analysis/upload.html')
