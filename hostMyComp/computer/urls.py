from django.urls import path
from . import views

urlpatterns = [
    path("", views.computer, name="local computer"),
]