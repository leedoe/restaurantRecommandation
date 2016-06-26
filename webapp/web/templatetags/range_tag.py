from django.template import Library

register = Library()

@register.filter
def get_range(value):
    return range(value)

@register.filter
def sub(value):
    return value - arg
