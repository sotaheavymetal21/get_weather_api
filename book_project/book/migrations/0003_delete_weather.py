# Generated by Django 4.1.5 on 2023-01-23 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0002_weather_alter_book_overview"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Weather",
        ),
    ]
