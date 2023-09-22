
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("outro", views.outro, name="outro"),
    path("exibe/", views.exib, name="exibe")
]
