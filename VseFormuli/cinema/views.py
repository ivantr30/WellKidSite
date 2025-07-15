from django.shortcuts import render
from .models import Video
from .forms import addVideoForm

# Create your views here.
def cinema(request):
    videos = Video.objects.all()
    return render(request, "cinema/cinema.html", context={"videos":videos})
def addVideos(request):
    form = addVideoForm()
    if request.method == "POST":
        form = addVideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return cinema(request)
    return render(request, "cinema/addVideo.html", {"form" : form})