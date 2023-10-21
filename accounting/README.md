# Accounting Project

Welcome to the Accounting Project, a Django-based web application for managing financial transactions and accounts.

## Project Structure

### Django Project: `accounting_project`

The "accounting_project" directory represents your Django project. It is the top-level directory for your project.

#### Project Files:

- `__init__.py`: An empty Python file that indicates this directory should be treated as a Python package.
- `asgi.py`: ASGI (Asynchronous Server Gateway Interface) entry point for your project.
- `settings.py`: Configuration settings for your Django project.
- `urls.py`: URL configuration for your project.
- `wsgi.py`: WSGI (Web Server Gateway Interface) entry point for your project.

### Django App: `accounting`

The "accounting" directory represents your Django app named "accounting." This app contains functionality related to accounting and financial transactions.

#### App Files and Directories:

- `migrations`: Directory where database migration files are stored.
- `templates`: Directory for storing HTML templates.
  - `accounting`: Subdirectory for templates specific to the "accounting" app.
    - `landing_page.html`: HTML template for the landing page.
    - `print_data.html`: HTML template for printing transaction data.
    - `upload_csv.html`: HTML template for uploading CSV files.
- `__init__.py`: An empty Python file that indicates this directory should be treated as a Python package.
- `admin.py`: Configuration of the Django admin interface for the "accounting" app.
- `apps.py`: Configuration of the "accounting" app.
- `forms.py`: Definition of forms used in the "accounting" app.
- `models.py`: Definition of data models for the "accounting" app, including the Account, Category, Transaction, and TransactionCSV models.
- `tests.py`: Unit tests for the "accounting" app.
- `urls.py`: URL configuration specific to the "accounting" app.
- `views.py`: Definition of views and view functions for the "accounting" app.

## Getting Started

To run this Django project, follow these steps:

1. Ensure you have Python and Django installed on your system.
2. Clone this project repository to your local machine.
3. Navigate to the "accounting_project" directory using the command line.
4. Run the following commands:

   ```bash
   # Apply database migrations
   python manage.py migrate

   # Start the development server
   python manage.py runserver
    ```
## Use Cases

### User Registration and Authentication
- **Description:** Users can create accounts, log in, and manage their personal information.
- **Actors:** User, System

#### Instructions
1. To create an account, click on the "Sign Up" or "Register" link on the landing page.
2. Provide the required information, including your email and password.
3. After successful registration, you can log in using your credentials.
4. Manage your personal information through the "Profile" section once logged in.

### View Landing Page
- **Description:** Users can access the application's landing page, which provides an overview of the available features and options.
- **Actors:** User

#### Instructions
1. Visit the application's URL.
2. You will be directed to the landing page, where you can explore the available features and options.

### Upload CSV File
- **Description:** Users can upload CSV files containing financial data for processing and storage within the system.
- **Actors:** User

#### Instructions
1. Navigate to the "Upload" or "Import Data" section of the application.
2. Select the CSV file you want to upload.
3. The system will process and store the data for further use.

### Print Data from CSV File
- **Description:** Users can print or generate reports based on the data stored in the CSV files, allowing for a physical or digital record of financial transactions.
- **Actors:** User

#### Instructions
1. Navigate to the "Reports" or "Print" section.
2. Select the desired data source (CSV file) and the report format.
3. Generate and print the report for your records.

### Manage Transaction Data (Admin)
- **Description:** Administrators can perform various actions related to transaction data, including adding, editing, deleting, and categorizing transactions, as well as resolving double booking issues.
- **Actors:** Administrator, System

#### Instructions
1. Log in as an administrator with the appropriate privileges.
2. Access the "Admin" or "Management" section of the application.
3. Perform actions like adding, editing, categorizing, and resolving double booking issues.

(Continue the structure above for the remaining use cases)

## Getting Started

To run this Accounting Application, follow these steps:

1. Ensure you have Python and the required dependencies installed on your system.
2. Clone this project repository to your local machine.
3. Set up the project configuration, including the database connection and system settings.
4. Run the application using the provided commands.

## Contributing
If you'd like to contribute to this project, please follow our [Contributing Guidelines](CONTRIBUTING.md).

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
If you have any questions or need assistance, please contact our support team at support@example.com.


# Django Accounting Project Structure

This document provides an explanation of the components and structure of the Django accounting project.

## Components
### 1. `settings.py`

- Settings (settings.py): This is the Django project's configuration file. It contains settings such as database configuration, installed apps, middleware, and more. Here's a summary of the important settings:
    - SECRET_KEY: A secret key for the project.
    - DEBUG: Debug mode (enabled for development, should be disabled in production).
    - ALLOWED_HOSTS: List of allowed hosts (empty for development).
    - INSTALLED_APPS: List of installed Django apps.
    - MEDIA_ROOT and MEDIA_URL: Settings for handling media files.
    - DATABASES: Configuration for the SQLite database.
    - TEMPLATES: Template engine configuration.
    - STATIC_URL: URL for serving static files.

### 2. `urls.py`

- URL Configuration (urls.py): This file defines URL patterns for the project. In your case, it includes paths for the admin panel and includes the accounting.urls for the accounting app.

### 3. `accounting` (Directory)

- Accounting App (accounting): This app appears to be the core of the project. It includes several components:
    - Views (views.py): These functions define the views for your app, such as the landing page, CSV file upload, and printing data.
    - Models (models.py): This file defines the data models for your app, including Account, Category, Transaction, and TransactionCSV.
    - Forms (forms.py): This file includes a form for uploading CSV files.
    - Templates (templates/): Contains HTML templates for rendering pages, including the landing page, printing transaction data, and uploading CSV files.

### 4. `views.py` (inside `accounting` app)

- Contains view functions that handle HTTP requests and render HTML templates.
- Key functions include `landing_page`, `upload_csv`, `print_data`, and `calculate_account_balances`.

### 5. `models.py` (inside `accounting` app)

- Defines the database schema for the accounting app.
- Includes models for `Account`, `Category`, `Transaction`, and `TransactionCSV`.

### 6. `forms.py` (inside `accounting` app)

- Defines a form for uploading CSV files. Used in the `upload_csv` view.

### 7. Templates (inside `accounting` app)

- Contains HTML templates for rendering views.
- Key templates include `landing_page.html`, `print_data.html`, and `upload_csv.html`.

### 8. `media` (Directory)

- Configured to store uploaded media files, such as CSV files.

### 9. `db.sqlite3`

- SQLite database file used for development.
- Stores data for accounts, transactions, categories, and uploaded CSV files.

## Database Structure

1. **Account Model**
   - Represents financial accounts with attributes like `name` and `balance`.

2. **Category Model**
   - Represents transaction categories with a `name` attribute.

3. **Transaction Model**
   - Represents individual transactions with attributes including `date`, `description`, `amount`, `account`, `category`, and `balance`.

4. **TransactionCSV Model**
   - Stores information about uploaded CSV files, including the file itself (`file`) and the upload timestamp (`uploaded_at`).

## Architecture

- The project follows the Model-View-Controller (MVC) architectural pattern.
- Model (M): Database models define data structure and relationships.
- View (V): View functions in `views.py` handle user requests and return HTML templates.
- Controller (C): URL routing (`urls.py`) directs requests to the appropriate view functions.
- Templates: HTML templates in the `templates` directory define the structure of web pages and data presentation.
- Database: SQLite is used to store financial data, transaction details, and uploaded CSV files.
- Media Handling: Uploaded CSV files are stored in the `media` directory.

## Project Overview

This project allows users to upload financial data in CSV format, process and save it to the database, and provides views to display transaction details and account balances. It includes a landing page displaying uploaded files and an option to upload new CSV files. The project can be expanded with additional features to enhance financial data management.

For more details on the code and specific functions, please refer to the actual code files within the project.



# Class Diagram

## Classes

### Account
- Fields: name, balance
- Methods: str()

### Category
- Fields: name

### Transaction
- Fields: date, description, amount, account, category, balance
- Associations: Transaction is associated with Account (ForeignKey), Category (ForeignKey)

### TransactionCSV
- Fields: file, uploaded_at
- Methods: str()

## Associations

- Transaction is associated with Account and Category. It seems like you have foreign keys in the Transaction class, which means a Transaction is linked to an Account and a Category.
- TransactionCSV is associated with a File. This suggests that TransactionCSV has a relationship with some other class or object named "File."


#
## Activate enviroment 
 ```bash
 /Users/christianashimitra/anaconda3/bin/activate && conda activate /Users/christianashimitra/anaconda3/envs/MachineLearningTraining; 
 ```