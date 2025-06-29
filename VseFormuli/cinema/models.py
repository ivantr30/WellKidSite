from django.db import models

# Create your models here.
class Video(models.Model):
    url = models.TextField("url")
    title = models.CharField("title", max_length=50)
    preview = models.ImageField("preview")
    category = models.CharField("category", max_length=50, default="Math")
    class Meta():
        verbose_name = "Video"
        verbose_name_plural = "Videos"