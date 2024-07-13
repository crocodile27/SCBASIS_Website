# forms.py

from django import forms
from .models import (
    Courses,
    Competitions,
)  # Assuming you have a Competitions model as well


class CourseForm(forms.Form):
    class Meta:
        model = Courses
        fields = [
            "name_of_course",
            "author",
            "course_description",
            "course_category",
            "url_of_image",
        ]

    name_of_course = forms.CharField(label="Name Of Course:", max_length=100)
    author = forms.CharField(label="Author:", max_length=100)
    course_description = forms.FileField(label="course_description")


class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competitions
        fields = [
            "name_of_competition",
            "author",
            "competition_description",
            "competition_category",
            "url_of_image",
        ]
