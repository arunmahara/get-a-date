from django.urls import path
from . import views

urlpatterns = [
    path("", views.ask, name="index"),
    path("denial/", views.denial, name="denial"),
    path("denial2/", views.denial2, name="denial2"),
    path("denial3/", views.denial3, name="denial3"),
    path("acceptence/", views.acceptence, name="acceptence"),
]
