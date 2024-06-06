from django.urls import path
from django_gcp_iap_auth import views


urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]
