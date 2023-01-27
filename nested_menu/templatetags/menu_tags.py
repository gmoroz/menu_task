from django import template
from django.shortcuts import get_object_or_404
from ..models import Menu


register = template.Library()


@register.inclusion_tag("tree_menu.html", takes_context=True)
def draw_menu(context, menu_title):
    context["menu"] = get_object_or_404(Menu, title=menu_title)
    