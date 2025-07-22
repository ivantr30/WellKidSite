from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Video(models.Model):
    video = models.FileField("file", upload_to='media/', validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv', 'wmv'])])  # noqa: F821
    title = models.CharField("title", max_length=50)
    preview = models.ImageField("preview", upload_to='media/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'PNG', 'webp'])])
    CATEGORIES = {'Math' :'Math', 'Geometry' : 'Geometry', 'Physics' : 'Physics', 'Algebra' : 'Algebra'}
    category = models.CharField("category", max_length=50, default="Math", choices=CATEGORIES)
    class Meta():
        verbose_name = "Video"
        verbose_name_plural = "Videos"