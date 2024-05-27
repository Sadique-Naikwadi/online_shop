from django import template

register = template.Library()

@register.filter
def custom_len(obj):
    """
    Custom template filter to call overridden len function.
    """
    return len(obj)
