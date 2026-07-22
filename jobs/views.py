from django.shortcuts import render, redirect
from .models import Job, StudentProfile


def home(request):
    jobs = Job.objects.all()
    return render(request, "home.html", {"jobs": jobs})


def apply(request, job_id):
    return redirect("profile")


def profile(request):

    if request.method == "POST":

        StudentProfile.objects.create(
            full_name=request.POST.get("full_name"),
            phone=request.POST.get("phone"),
            skills=request.POST.get("skills"),
            resume=request.FILES.get("resume")
        )

        return redirect("home")

    return render(request, "profile.html")