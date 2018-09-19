from django.db import models

class Blockchain(models.Model):

    value = models.IntegerField()
    total = models.IntegerField(default=0, editable=False)
    processed = models.BooleanField(default=False, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    