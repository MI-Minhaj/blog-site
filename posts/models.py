from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    publish_date = models.DateField()


class Comment(models.Model):
    content = models.TextField()