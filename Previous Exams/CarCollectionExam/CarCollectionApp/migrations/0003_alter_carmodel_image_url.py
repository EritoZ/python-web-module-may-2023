# Generated by Django 4.2.2 on 2023-06-19 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarCollectionApp', '0002_alter_carmodel_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='image_url',
            field=models.URLField(),
        ),
    ]