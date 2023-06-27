from django.core.exceptions import ValidationError


def first_letter_validator(value: str):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")


def fruit_all_letters_validator(value: str):
    if not value.isalpha():
        raise ValidationError("Fruit name should contain only letters!")
