# Generated by Django 4.2.2 on 2023-06-24 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruitApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='image_url',
            field=models.URLField(blank=True, default=False),
            preserve_default=False,
        ),
    ]