from django.db import models

class Record(models.Model):
    name = models.TextField()
    description = models.TextField()
    startTime = models.TextField()
    endTime = models.TextField()
    userId = models.TextField()
