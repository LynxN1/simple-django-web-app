from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
