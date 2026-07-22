from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    salary = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class StudentProfile(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    skills = models.TextField()
    resume = models.FileField(upload_to="resumes/")

    def __str__(self):
        return self.full_name