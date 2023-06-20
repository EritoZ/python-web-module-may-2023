from django.db import models
from django.core import validators


# Create your models here.
class ProfileModel(models.Model):
    username = models.CharField(
        max_length=15,
        validators=(
            validators.MinLengthValidator(2),
            validators.RegexValidator(regex=r'^\w+$', message="Ensure this value contains only letters, "
                                                              "numbers, and underscore.")
        )
    )
    email = models.EmailField()

    age = models.IntegerField(
        blank=True,
        null=True,
        validators=(
            validators.MinValueValidator(0),
        )
    )


class AlbumModel(models.Model):
    genres = (
        ('Pop Music', 'Pop Music'),
        ('Jazz Music', 'Jazz Music'),
        ('R&B Music', 'R&B Music'),
        ('Rock Music', 'Rock Music'),
        ('Country Music', 'Country Music'),
        ('Dance Music', 'Dance Music'),
        ('Hip Hop Music', 'Hip Hop Music'),
        ('Other', 'Other'),
    )
    album_name = models.CharField(
        max_length=30,
        unique=True,
        error_messages={
            'unique': 'Your album name is too common!'
        }
    )

    artist = models.CharField(
        max_length=30
    )

    genre = models.CharField(
        max_length=30,
        choices=genres
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=(
            validators.MinValueValidator(0.0),
        )
    )
