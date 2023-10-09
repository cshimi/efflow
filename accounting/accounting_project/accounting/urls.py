# your_app_name/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('landing_page/', views.landing_page, name='landing_page'),
    path('upload_csv/', views.upload_csv, name='upload_csv'),
    path('print_data/', views.print_data, name='print_data'),
]
