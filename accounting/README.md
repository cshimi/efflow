# Django Accounting Application

A simple accounting web application built with Django.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Features

- Create and manage accounts.
- Add, edit, and categorize transactions.
- View transaction history.
- Authentication system (requires user login).

## Getting Started

### Prerequisites

- Python 3.x
- Django 3.x
- A compatible database (e.g., PostgreSQL, MySQL, SQLite)

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/django-accounting-app.git
   cd django-accounting-app
   ```
2. Activate enviroment 
```bash
. /Users/christianashimitra/anaconda3/bin/activate && conda activate /Users/christianashimitra/anaconda3/envs/MachineLearningTraining;
```
   
3. Create a new Django project:
   ```bash
    django-admin startproject accounting_project
    cd accounting_project
   ```
3. Inside your project, create a Django app for your accounting application:
   ```bash
    python manage.py startapp accounting
   ```

4. Create an HTML Template:
   ```bash
    your_app_name/
    ├── templates/
    │   └── your_app_name/
    └── ...
   ```
5. create landing_page.html
6. Create a View:In your app's views.py file, create a view function that will render the landing_page.html template.
   ```bash
    # your_app_name/views.py

    from django.shortcuts import render

    def landing_page(request):
        return render(request, 'your_app_name/landing_page.html')
   ```
7. Create a URL Pattern: In your app's urls.py file, create a URL pattern that maps to the landing_page view.
   ```bash
   # your_app_name/urls.py

    from django.urls import path
    from . import views

    urlpatterns = [
      path('', views.landing_page, name='landing_page'),
    ]
   ```

8. Configure Project URLs:In your project's urls.py file, include the URLs of your app.
```bash
  # project_name/urls.py

  from django.contrib import admin
  from django.urls import include, path

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('', include('your_app_name.urls')),
  ]
```
9. Add the app in settings.py 
```bash
INSTALLED_APPS = [
    # ...
    'your_project_name.your_app_name',
    # ...
]
```

commit the first commit for the accounting project