from django.db import models
from django.core.validators import MinLengthValidator
from validators import capital_letter_validator, only_letters_validator


# Create your models here.

class UserProfile(models.Model):
    username = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(2)]
    )

    first_name = models.CharField(
        max_length=20,
        validators=[capital_letter_validator]
    )

    last_name = models.CharField(
        max_length=20,
        validators=[capital_letter_validator]
    )

    profile_picture = models.URLField(
        blank=True
    )


class Plant(models.Model):
    types = [
        ('Outdoor Plants', 'Outdoor Plants'),
        ('Indoor Plants', 'Indoor Plants')
    ]

    type = models.CharField(
        max_length=14,
        choices=types,
    )

    name = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(2), only_letters_validator],
    )

    image = models.URLField()

    description = models.TextField()

    price = models.FloatField()