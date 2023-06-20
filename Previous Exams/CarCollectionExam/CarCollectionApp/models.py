from django.db import models
from django.core import validators


# Create your models here.
class ProfileModel(models.Model):
    username = models.CharField(
        max_length=10,
        validators=[validators.MinLengthValidator(2, message="The username must be a minimum of 2 chars")]
    )
    email = models.EmailField()

    age = models.IntegerField(
        validators=[validators.MinValueValidator(18)]
    )

    password = models.CharField(
        max_length=30
    )

    first_name = models.CharField(
        blank=True,
        max_length=30
    )

    last_name = models.CharField(
        blank=True,
        max_length=30
    )

    profile_picture = models.URLField(
        blank=True
    )


class CarModel(models.Model):
    types = (
        ("Sports Car", "Sports Car"),
        ("Pickup", "Pickup"),
        ("Crossover", "Crossover"),
        ("Minibus", "Minibus"),
        ("Other", "Other"),
    )

    type = models.CharField(
        max_length=10,
        choices=types,
    )

    model = models.CharField(
        max_length=20,
        validators=[validators.MinLengthValidator(2)]
    )

    year = models.IntegerField(
        validators=[
            validators.MinValueValidator(1980, message="Year must be between 1980 and 2049"),
            validators.MaxValueValidator(2049, message="Year must be between 1980 and 2049")
        ]
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=[validators.MinValueValidator(1)]
    )
