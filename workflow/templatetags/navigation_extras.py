from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag
def active_nav(request, urls):
    if request.path in ( reverse(url) for url in urls.split() ):
        return "active"
    return ""