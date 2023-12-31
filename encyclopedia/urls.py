from django.urls import path

from . import views

app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wiki, name="wiki"),
]
