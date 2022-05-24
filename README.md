# django-custom-url
django-custom-url is a Django app to **easily manage custom url linked to static files**.

Django is a great framework, but if you want to create URLs linked static files like PDF or images, you have 
to create a view for that purpose. And if you have to manage, not just one but various of this URLs, you will end up
with a bunch of dummy views.

This app allows you to create a custom URL and upload a file linked to that URL, so that when a user requests
the URL, they can view or download the related file (depending on whether it is a valid format for viewing from the browser).

---

## How it works
There is possible to use this app in two ways:
1. Use a fallback view that will check for a custom URL if all other URL patterns fails.
   This options doesn't require restarting your application server, just adding the custom URLs in the admin site, and it will work.
2. Execute an administrative command after creating the custom URLs in the admin, which will harcode URLs in a urls.py file.
   This option require restarting you application server each time a URL is added or modified.

---

## Installation
1. Run `pip install django-custom-url`
2. Add `custom_url` to `settings.INSTALLED_APPS` like this:
```python
    INSTALLED_APPS = [
        ...
        'custom_url',
    ]
```
3. Run `python manage.py migrate`

## Setup
If you want to use the fallback view (option 1 of the "How it works" section):

1. Include the Custom URL view in your project urls.py. Include it at the end of the path list like this:
```python
    from custom_url.views import CustomUrlView

    urlpatterns = [
        ...
        path('<path:url>', CustomUrlView.as_view())
    ]
```


If you want to opt for the hardcoded URLs (option 2 of the "How it works" section):

1. Include the Custom URL URLconf in your project urls.py like this:
```python
    from django.urls import include
    urlpatterns = [
        ...
        path('', include('custom_url.urls'))
    ]
```
2. Create your custom URLs in the admin site.
3. Run `python .\manage.py  update_urls` to update the Custom URL urls.py file.


---

## License
Released under [MIT License](LICENSE).

---

## Support
If you are having issues, please let me know through raising an issue, or just sending me a DM to [@luciano_dev](https://twitter.com/luciano_dev).