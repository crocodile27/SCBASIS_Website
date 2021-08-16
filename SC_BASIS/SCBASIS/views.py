from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import markdown

from .models import User, Courses, Competitions

# Create your views here.

def index(request):
	return render(request, 'scbasis/index.html')

def course_guides(request):
    math_courses = Courses.objects.filter(course_category="Math")
    english_courses = Courses.objects.filter(course_category="English")
    science_courses = Courses.objects.filter(course_category="Science")
    humanities_courses = Courses.objects.filter(course_category="Humanities")
    other_courses = Courses.objects.filter(course_category="Others")
    return render(request, 'scbasis/course_guides.html', {
        "math_courses":math_courses,
        "english_courses":english_courses,
        "science_courses":science_courses,
        "humanities_courses":humanities_courses,
        "other_courses":other_courses,
    })

def competition_guides(request):
    math_competitions = Competitions.objects.filter(competition_category="Math")
    economic_competitions = Competitions.objects.filter(competition_category="Economic")
    biology_competitions = Competitions.objects.filter(competition_category="Biology")
    chemistry_competitions = Competitions.objects.filter(competition_category="Chemistry")
    physics_competitions = Competitions.objects.filter(competition_category="Physics")
    return render(request, 'scbasis/competition_guides.html',{
        "math_competitions": math_competitions,
        "economic_competitions": economic_competitions,
        "biology_competitions": biology_competitions,
        "chemistry_competitions": chemistry_competitions,
        "physics_competitions": physics_competitions,
        })

def create_guides(request):
    return render(request, 'scbasis/create_guides.html')

def submit_courses(request):
    if request.method == "POST":
        name_of_course = request.POST['name_of_course']
        author = request.POST['author']
        course_description = request.FILES['course_description']
        editor = request.user
        course_category = request.POST['course_category']
        url_of_image = request.POST['image_url']

        course = Courses(name_of_course=name_of_course, author=author, course_description=course_description, editor=editor, course_category=course_category, url_of_image=url_of_image)
        course.save()
        
        return HttpResponseRedirect(reverse("index"))
        #User is returned to the index page
    return render(request, "scbasis/create_guides.html")
    #or else they are asked to retry to create a listing.

def submit_competitions(request):
    if request.method == "POST":
        name_of_competition = request.POST['name_of_competition']
        author=request.POST['author']
        competition_description = request.POST['competition_description']
        editor = request.user
        competition_category = request.POST['competition_category']
        url_of_image = request.POST['image_url']

        competition = Competitions(name_of_competition=name_of_competition, author=author, competition_description=competition_description, editor=editor, competition_category=competition_category, url_of_image=url_of_image)
        competition.save()
        
        return HttpResponseRedirect(reverse("index"))
        #User is returned to the index page
    return render(request, "scbasis/create_guides.html")
    #or else they are asked to retry to create a listing.



def display_courses(request, course_id):
    guide = Courses.objects.get(pk=course_id)
    title=guide.course_description.read().decode("utf-8")
    course_description=markdown.markdown(title) if title else None
    return render(request, 'scbasis/display_courses.html',{
        "guide":guide,
        "course_description":course_description,
        })

def display_competitions(request, competition_id):
    guide = Competitions.objects.get(pk=competition_id)
    return render(request, 'scbasis/display_competitions.html',{
        "guide":guide,
        })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "scbasis/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "scbasis/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "scbasis/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "scbasis/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "scbasis/register.html")
