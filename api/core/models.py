from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

class Data(models.Model):
    """Комментарии"""
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    img = models.ImageField(upload_to="core/")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='data_user', default=1)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)