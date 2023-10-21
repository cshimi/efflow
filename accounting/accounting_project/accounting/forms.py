# forms.py - This file defines forms for user input and validation.

from django import forms
from .models import TransactionCSV  # Import the TransactionCSV model

# Forms define the structure of HTML forms for capturing user input.
# Form fields correspond to input fields in the HTML form.



# TransactionCSVUploadForm: A form for uploading CSV files.
class TransactionCSVUploadForm(forms.ModelForm):
    class Meta:
        model = TransactionCSV  # The form is based on the TransactionCSV model.
        fields = ['file']  # It includes a field for the 'file' attribute in the model.

# TransactionFilterForm: A form for filtering transaction data.
class TransactionFilterForm(forms.Form):
    start_date = forms.DateField(label='Start Date', required=False)  # Field for start date
    end_date = forms.DateField(label='End Date', required=False)      # Field for end date
    notification_text = forms.CharField(max_length=200, required=False)  # Field for notification text
    min_amount = forms.DecimalField(label='Minimum Amount', required=False)  # Field for minimum amount
    max_amount = forms.DecimalField(label='Maximum Amount', required=False)  # Field for maximum amount

    # These form fields correspond to filtering criteria for transaction data.
    # They allow users to filter data based on start date, end date, notification text, and amount.
