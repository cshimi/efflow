from django.db import models

# Define a model to store uploaded CSV files
class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')  # FileField to store the uploaded CSV file
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the file was uploaded
