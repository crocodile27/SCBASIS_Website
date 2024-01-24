from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime, date


class User(AbstractUser):
    pass

class Courses(models.Model):
    name_of_course = models.CharField(max_length=32)
    course_description = models.FileField(upload_to='course_guides')
    editor = models.ForeignKey(User, on_delete = models.CASCADE, related_name="courses", default = None)
    author = models.CharField(max_length=50, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now = False, blank=True)
    course_category = models.CharField(max_length=50)
    url_of_image = models.CharField(max_length=800)
    viewable = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return self.name_of_course

class Competitions(models.Model):
    name_of_competition = models.CharField(max_length=32)
    competition_description = models.FileField(upload_to='competition_guides')
    editor = models.ForeignKey(User, on_delete = models.CASCADE, related_name="competitions", default = None)
    author = models.CharField(max_length=50, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now = False, blank=True)
    competition_category = models.CharField(max_length=50)
    url_of_image = models.CharField(max_length=800)
    viewable = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return self.name_of_competition