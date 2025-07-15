from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Video(models.Model):
    video = models.FileField("file", default=None, null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv', 'wmv'])])  # noqa: F821
    title = models.CharField("title", max_length=50)
    preview = models.ImageField("preview", validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'PNG'])])
    category = models.CharField("category", max_length=50, default="Math")
    class Meta():
        verbose_name = "Video"
        verbose_name_plural = "Videos"