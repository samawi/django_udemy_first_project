from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.topic_name

class WebPage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    web_name = models.CharField(max_length=256)
    url_address = models.URLField(unique=True)

    def __str__(self):
        return self.web_name

class AccessRecord(models.Model):
    name = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    date_accessed = models.DateTimeField()

    def __str__(self):
        return str(self.date_accessed)