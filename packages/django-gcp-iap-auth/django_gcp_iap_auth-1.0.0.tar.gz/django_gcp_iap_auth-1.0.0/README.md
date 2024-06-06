# Quickstart

## Server

```
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser --username test --email test@gmail.com --no-input
python manage.py runserver
```

## Client

In another terminal, this query should return `{"message": "Hello test"}`:
```
curl -H "X-Goog-Authenticated-User-Email: accounts.google.com:test@gmail.com" http://localhost:8000/gcp_iap_proxy
```

On the other hand, the following query should return `{"message": "Hello unauthenticated user"}`:
```
curl -H "X-Goog-Authenticated-User-Email: accounts.google.com:unknown@gmail.com" http://localhost:8000/gcp_iap_proxy
```

## Resources

The project layout is inspired of https://realpython.com/installable-django-app/ and
https://github.com/realpython/django-receipts. The django application lives in a repository with a working django
project for testing purposes.

Google Cloud's documentation about [how to retrieve the user's identity on its IAP proxy](https://cloud.google.com/iap/docs/identity-howto).
