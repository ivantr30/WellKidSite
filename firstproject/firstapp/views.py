from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def function(request):
    return HttpResponse("Hallo")
def formulas(request):
    return render(request,template_name='index.html')
def mathformulas(request):
    return render(request,template_name='math.html')