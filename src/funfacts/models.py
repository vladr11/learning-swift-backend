from django.db import models


class FunFact(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=4095)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
