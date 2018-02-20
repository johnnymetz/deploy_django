from django.db import models


class Athlete(models.Model):
    name = models.CharField(max_length=110, unique=True)
    ppg = models.FloatField()
    active = models.BooleanField()

    def __str__(self):
        return self.name
