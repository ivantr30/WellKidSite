from django.urls import path
from . import views

urlpatterns = [
    path('function', views.function),
    path('formulas', views.formulas),
    path('mathformulas', views.mathformulas),
]