from django.shortcuts import render

# Create your views here.
def cinema(request):
    return render(request, "cinema/cinema.html")