from django.urls import path
from . import views

urlpatterns = [
    path("", views.menu_show, name="index"),
    path("<slug:url>/", views.menu_show, name="index"),
]
