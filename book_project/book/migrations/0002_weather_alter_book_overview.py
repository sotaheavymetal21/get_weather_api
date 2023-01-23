# Generated by Django 4.1.5 on 2023-01-23 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Weather",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("location", models.CharField(max_length=32)),
                ("weather", models.CharField(max_length=32)),
                ("temperature", models.IntegerField()),
            ],
            options={
                "verbose_name": "天気情報",
                "verbose_name_plural": "天気情報",
            },
        ),
        migrations.AlterField(
            model_name="book",
            name="overview",
            field=models.CharField(max_length=50),
        ),
    ]
