from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("apply/<int:job_id>/", views.apply, name="apply"),
    path("profile/", views.profile, name="profile"),
]