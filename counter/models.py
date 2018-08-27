from django.db import models

# Create your models here.
class Counter(models.Model):
    counter = models.IntegerField(default=0)
    url = models.CharField(max_lenght=2000)
    def __str__(self):
        return self.counterName
