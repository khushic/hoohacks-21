from django import template

register = template.Library()

@register.filter
def tag_to_class(value):
    return value.lower().replace(" ", "-")
