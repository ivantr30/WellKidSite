from django.shortcuts import render
from .models import Video

# Create your views here.
def cinema(request):
    videos = Video.objects.all()
    return render(request, "cinema/cinema.html", context={"videos":videos})
def addVideos(request):
    return render(request, "cinema/addVideo.html")