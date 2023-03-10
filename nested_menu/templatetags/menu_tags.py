from django import template
from django.shortcuts import get_object_or_404
from ..models import Menu
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.inclusion_tag("tree_menu.html", takes_context=True)
def draw_menu(context, menu_title):
    context["menu"] = get_object_or_404(Menu, title__iexact=menu_title, parent=None)
    request_url = context["request"].path
    try:
        active_menu = Menu.objects.get(url=request_url)
    except ObjectDoesNotExist:
        pass
    else:
        context["expanded_menus"] = [
            parent.id for parent in active_menu.get_parents()
        ] + [active_menu.id]
    return context


@register.inclusion_tag("tree_menu.html", takes_context=True)
def draw_children_menu(context, menu_id):
    context["menu"] = get_object_or_404(Menu, pk=menu_id)
    return context


@register.filter
def get_hyphens(string, menu):
    """Данная функция помогает улучшить отображение вложенных объектов"""
    return string * len(menu.get_parents())
