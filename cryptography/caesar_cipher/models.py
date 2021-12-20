from django.db import models


class ccDB(models.Model):
    cipher = models.CharField(max_length=550)
    key = models.IntegerField()

    def __str__(self):
        return self.cipher