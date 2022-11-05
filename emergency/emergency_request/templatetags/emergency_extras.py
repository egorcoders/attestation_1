from django import template

register = template.Library()


@register.simple_tag
def get_verbose_name(obj):
    return obj._meta.verbose_name
