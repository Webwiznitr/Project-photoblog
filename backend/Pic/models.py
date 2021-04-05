from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField()
    pub_date = models.DateTimeField('date published')


class Caption(models.Model):
    caption_text = models.TextField(max_length=200)
