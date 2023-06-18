import re

from django.core.exceptions import ValidationError


def capital_letter_validator(value: str):
    if not value[0].isupper():
        raise ValidationError("Your name must start with a capital letter!")


def only_letters_validator(value: str):
    valid_field = re.match(r'^[a-z A-Z]+$', value)

    if not valid_field or value.isspace():
        raise ValidationError("Plant name should contain only letters and spaces!")
