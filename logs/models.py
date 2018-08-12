from django.db import models

# Create your models here.
class Logs(models.Model):
    log_text = models.CharField(max_length=2000)
    data = models.DateTimeField('published')
    def __str__(self):
        return self.log_text
