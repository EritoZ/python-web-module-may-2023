# Generated by Django 4.2.2 on 2023-06-24 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruitApp', '0003_alter_profilemodel_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruitmodel',
            name='nutrition',
            field=models.TextField(blank=True),
        ),
    ]