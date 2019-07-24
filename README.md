# bt_real_estate
A platform to sell real estate properties (powered by Django).

## Features included
 - Display real estate properties for sale with pictures and detailed information about the property.
 - User registration with a dashboard for the user to keep track of properties they have inquired about.
 - Search real estate properties with filters.
 - Realtor registration from the admin panel.
 - Linking the property listing with the realtor.
 - Inquiry form for registered users and site visitors to inquire about properties listed, with email notifications.
  
## The platform has the following main components
 - **btre** - This is the main folder of the app which contains the settings.py file.
 - **Pages** - This app serves the static pages of the site.
 -  **Realtors** - This app manages the data of realtors. It is used for administration only hence it does not have any public views.
 - **Contacts** - This app manages the inquiries coming from the site visitors interested in the real estate property.
 - **Accounts** - This app manages site visitors who want to become registered users of the site.
 - **Listings** - This app manages the real estate listings of properties available for sale.

## The site was developed with the following technologies
 - Python 3.7.3
 - Django Framework 2.2.3
 - PostgreSQL 11
 - Boostrap
 - A detailed list of requirements can also be found at [requirements.txt](https://github.com/Chandral/bt_real_estate/blob/master/requirements.txt)

## Installation
 - Install PostgreSQL. [Click here](https://www.postgresql.org/download/) to download PostgreSQL.
 - Create a virtual environment for Python. [Click here](https://docs.python.org/3/tutorial/venv.html) to learn more about virtual environments in Python.
 - Clone this repository to your machine. [Click here](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository) and refer the "Cloning an Existing Repository" section of the page.
 - Once you have completed the steps above and activated the virtual environment in your command line, go to the folder which contains the '*manage.py*' file. Run the Django commands with 'manage.py' required to configure/migrate database, static and media files on your machine. E.g. ```python manage.py makemigrations```, ```python manage.py migrate``` ```python manage.py collectstatic```etc.
 - Please note that the '*settings.py*' file of the '*btre*' folder gets the data for sensitive fields such as SECRET_KEY, EMAIL_HOST_PASSWORD etc. from an external YAML file which is not included in this repo. The YAML file is excluded on purpose to protect the data from being publicly available on repos such as this one.
 - Once everything is setup correctly, run ```python manage.py runserver``` command from the same folder. Your app should be running locally on the default localhost port 8000.

## Support
 - For any questions please, send an email to chandral.thakor@gmail.com
