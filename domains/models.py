from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from settings.models import City, State, Country
# Create your models here.

class Domain(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # FIXME: CASCADE To RESTRICT
    name = models.CharField(max_length=150, verbose_name='Domain Name')
    comment = models.TextField(null=True, blank=True)
    level = models.IntegerField(validators=[MaxValueValidator(20),MinValueValidator(1)], default=1)
    nameservers = models.JSONField(default=list)
    registrar_whois = models.CharField(max_length=256, null=True) # FIXME: Remove null=True
    is_public = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    


class Whois(models.Model):
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE) # FIXME: CASCADE To RESTRICT
    TYPE_OPTIONS = (
        (1, 'Registrant Contact'),
        (2, 'Administrative Contact'),
        (3, 'Technical Contact'),
    )
    whois_type = models.IntegerField(choices=TYPE_OPTIONS, default=1)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone = models.JSONField(default=list, null=True, blank=True)
    address = models.JSONField(default=list, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.RESTRICT, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.RESTRICT, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.RESTRICT, null=True, blank=True)
    postal_code = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Whois"
