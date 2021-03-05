from django.db import models

class Videos(models.Model):
    url = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    channelUrl = models.CharField(max_length=1000)
    channelTitle = models.CharField(max_length=1000)
    publishTime = models.CharField(max_length=1000)

    def __str__(self): return self.title
