# Generated by Django 4.2.2 on 2023-06-19 16:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=30)),
                ('artist', models.CharField(max_length=30)),
                ('genre', models.CharField(choices=[('Pop Music', 'Pop Music'), ('Jazz Music', 'Jazz Music'), ('R&B Music', 'R&B Music'), ('Rock Music', 'Rock Music'), ('Country Music', 'Country Music'), ('Dance Music', 'Dance Music'), ('Hip Hop Music', 'Hip Hop Music'), ('Other', 'Other')], max_length=30)),
                ('description', models.TextField(blank=True)),
                ('image_url', models.URLField()),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
            ],
        ),
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.RegexValidator(message='Ensure this value contains only letters, numbers, and underscore.', regex='^\\w+$')])),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]
