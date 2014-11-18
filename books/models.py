from django.db import models

class Book(models.Model):
  title = models.CharField(max_length = 1000)
  body = models.TextField()
  author = models.CharField(max_length = 1000, default='No author added')

  def __str__(self):
    return self.title