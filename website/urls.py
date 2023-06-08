from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:aID>", views.materialInfo),
    path("<str:sort>", views.indexWithSort)
]