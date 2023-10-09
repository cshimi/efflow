# your_app_name/views.py

from django.shortcuts import render

def landing_page(request):
    return render(request, 'accounting/landing_page.html')
