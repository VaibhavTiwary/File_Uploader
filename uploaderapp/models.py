from django.db import models


class FileData(models.Model):
    date = models.TextField()
    accno = models.TextField()
    state = models.TextField()
    pin = models.TextField()
    dpd = models.TextField()
