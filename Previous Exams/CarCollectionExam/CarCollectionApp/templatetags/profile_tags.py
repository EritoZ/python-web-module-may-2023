from django import template

from CarCollectionApp.models import ProfileModel

register = template.Library()


@register.simple_tag
def search_profile():
    return ProfileModel.objects.first()
