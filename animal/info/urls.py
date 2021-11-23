from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('family/<int:id>/',views.family,name='family_view'),
    path('animal/<int:id>/',views.animal,name='animal_view'),
    path('animals/',views.animals,name='animals_view')
]