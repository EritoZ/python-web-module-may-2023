# Generated by Django 4.2.2 on 2023-06-24 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruitApp', '0002_alter_profilemodel_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]