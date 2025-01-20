from django import template

register = template.Library()

@register.filter
def admin_urlname(value):
    # Implement the logic for the filter here
    return f"admin:{value}"
