from django.urls import path
from . import views

urlpatterns = [
    path("", views.menu_show, name="menu"),
    path("<slug:url>/", views.menu_show, name="menu"),
]
