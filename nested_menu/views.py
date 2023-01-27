from django.shortcuts import render


def menu_show(request, url=None):
    return render(request, "menu.html")
