from django.db import models

# Create your models here.
class Light(models.Model):
    count = models.IntegerField()

    def __str__(self):
        return self.count