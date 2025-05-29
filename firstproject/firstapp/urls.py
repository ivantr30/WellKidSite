from django.urls import path
from . import views

urlpatterns = [
    path('function', views.function),
    path('formulas', views.formulas),
    path('mathformulas', views.mathformulas),
    path('algebraformulas', views.algebraformulas),
    path('geometryformulas', views.geometryformulas),
    path('physicsformulas', views.physicsformulas),
    path('class', views.some_class.as_view()),
]