from django.forms import ModelForm
from .models import Video

class addVideoForm(ModelForm):
    class Meta:
        model = Video
        fields = "__all__"