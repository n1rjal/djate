from django.urls import path
from . import views


urlpatterns = [
    path("add/", views.Adder.as_view(), name="Adder view"),
]
