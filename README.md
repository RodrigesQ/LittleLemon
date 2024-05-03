# LittleLemon

LittleLemon Project Setup Guide

This guide provides step-by-step instructions to set up and initialize the LittleLemon project from the provided Git repository.
Cloning the Repository

Clone the LittleLemon repository from GitHub using the following command:

bash

git clone https://github.com/RodrigesQ/LittleLemon.git

Navigate to the project directory:

bash

cd LittleLemon

Setting Up Virtual Environment

Create a virtual environment named workspace:

python -m venv workspace

Activate the virtual environment:

    Windows (PowerShell):

    Set-ExecutionPolicy Bypass -Scope Process
    .\workspace\Scripts\Activate

Installing Dependencies

Install Django within the virtual environment:

pip install django

Initializing Django Project

Create a new Django project named littlelemon:

django-admin startproject littlelemon

Navigate to the project directory:

bash

cd littlelemon

Create a new app named restaurant:

python manage.py startapp restaurant

Configuring Settings

Open the settings.py file within the littlelemon project package and add the restaurant app to the INSTALLED_APPS list:

python

INSTALLED_APPS = [
    # Other installed apps...
    'restaurant',
]

Running the Development Server

Run the Django development server:

python manage.py runserver

MySQL Setup

    MySQL Workbench:
        Username: root
        Password: root

Create a new database named LittleLemon in MySQL.
Creating a Superuser

Create a superuser for the Django admin:

python manage.py createsuperuser

Generating Requirements File

Generate a requirements.txt file based on the installed packages:

pip freeze > requirements.txt

Install additional packages:

pip install -r requirements.txt

Accessing Admin Panel

Access the Django admin panel:

http://127.0.0.1:8000/admin/

Additional Setup (Optional)

For additional setup instructions, please refer to the provided documentation and configuration steps.

Feel free to adjust and expand upon this template based on your specific project requirements.
