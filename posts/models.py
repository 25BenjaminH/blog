from django.db import models

# Create your models here.
class Country_total_deaths(models.Model):
    country = models.CharField(max_length=255)
    deaths = models.IntegerField(max_length=255)
    def __str__(self):
        return self.country, self.deaths

    