from django.db import models

# Create your models here.
class Data(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=20, blank=True)
    population = models.IntegerField()

    def dump(self):
        return {
            'id': self.id,
            'year': self.year,
            'state': self.state,
            'population': self.population
        }