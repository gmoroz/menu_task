from django import template
from django.shortcuts import get_object_or_404
from ..models import Menu
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.inclusion_tag("tree_menu.html", takes_context=True)
def draw_menu(context, menu_title):
    context["menu"] = get_object_or_404(Menu, title=menu_title, parent=None)
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
