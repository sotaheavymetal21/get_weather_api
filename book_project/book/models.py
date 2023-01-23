from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    overview = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Weather(models.Model):
    location = models.CharField(max_length=32)
    weather = models.CharField(max_length=32)
    temperature = models.IntegerField()

    def __str__(self):
        return self.location

    class Meta:
        verbose_name = verbose_name_plural = "天気情報"
