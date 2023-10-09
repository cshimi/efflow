from django import forms
from .models import TransactionCSV  # Import the TransactionCSV model

class TransactionCSVUploadForm(forms.ModelForm):
    class Meta:
        model = TransactionCSV
        fields = ['file']
