from django.forms import ModelForm, TextInput
from .models import Video

class addVideoForm(ModelForm):
    class Meta:
        model = Video
        fields = "__all__"
        widgets = {
            'title' : TextInput(attrs={'placeholder' : 'Введите название'})
        }
        