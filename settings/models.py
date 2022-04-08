from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self) -> str:
        return self.name


class State(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name



class Country(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self) -> str:
        return self.name