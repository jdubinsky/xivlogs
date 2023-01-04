from django.db import models

class Ability(models.Model):
    ability_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=4096)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['ability_id']),
        ]

