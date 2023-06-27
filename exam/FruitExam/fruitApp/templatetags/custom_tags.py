from django import template

from fruitApp.models import ProfileModel

register = template.Library()


@register.simple_tag
def find_profile():
    return ProfileModel.objects.first()
