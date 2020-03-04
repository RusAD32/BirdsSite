from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path("", index_view, name="index"),
    path("strizh", strizh_view, name="strizhi"),
    path("contacts", contacts_view, name="contancts"),
]