from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), # Original entry.  References the index function in views
    path("<str:title>", views.contents, name="contents" )
]
