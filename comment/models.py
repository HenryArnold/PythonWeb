from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=200, default="nick")
    comment_text = models.CharField(max_length=2000)
    pub_data = models.DateTimeField('data published')
    def __str__(self):
        return self.comment_text
