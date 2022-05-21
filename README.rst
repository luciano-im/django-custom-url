==========
Custom URL
==========

Polls is a Django app to conduct web-based polls. For each question,
visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'custom_url',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('', include('custom_url.urls')),

3. Run ``python manage.py migrate`` to create the curstom_url models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a custom URL (you'll need the Admin app enabled).