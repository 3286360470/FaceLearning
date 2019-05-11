# from django.template import Variable, VariableDoesNotExist
from django import template

register = template.Library()

@register.simple_tag()
def whoami(front):
    return front%2 == 0