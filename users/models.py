from ipaddress import ip_address
from django.contrib.auth.models import User
from django.db import models
from domains.models import Domain
from .utils import generate_api_key
# Create your models here.


class ApiKey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    api_key = models.CharField(max_length=50, unique=True, null=True, blank=True) # FIXME: Delete null=True blank=True
    allowed_domains = models.ManyToManyField(Domain)
    allowed_ip = models.JSONField(default=list)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.api_key:
            self.api_key = generate_api_key()
        super().save(*args, **kwargs)