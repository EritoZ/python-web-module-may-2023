from django import template

from plantsApp.models import UserProfile

register = template.Library()


@register.simple_tag
def search_profile():
    return UserProfile.objects.first()
