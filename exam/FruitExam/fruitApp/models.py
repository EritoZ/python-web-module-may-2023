from django.db import models
from django.core import validators

import custom_validators


# Create your models here.
class ProfileModel(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=[validators.MinLengthValidator(2), custom_validators.first_letter_validator]
    )

    last_name = models.CharField(
        max_length=35,
        validators=[validators.MinLengthValidator(1), custom_validators.first_letter_validator]
    )

    email = models.EmailField(
        max_length=40
    )

    password = models.CharField(
        max_length=20,
        validators=[validators.MinLengthValidator(8)]
    )

    image_url = models.URLField(
        blank=True,
        null=True,
    )

    age = models.IntegerField(
        blank=True,
        null=True,
        default=18
    )


class FruitModel(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[validators.MinLengthValidator(2), custom_validators.fruit_all_letters_validator]
    )

    image_url = models.URLField()

    description = models.TextField()

    nutrition = models.TextField(
        blank=True,
    )
