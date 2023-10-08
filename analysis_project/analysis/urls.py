from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),  # URL for file upload
    path('display_file/<int:file_id>/', views.display_file, name='display_file'),
]
