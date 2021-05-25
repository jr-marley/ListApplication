from django.db import models


class Locate(models.Model):
    lat = models.CharField(max_length=200)
    lng = models.CharField(max_length=200)

    def __str__(self):
        return self.lat
