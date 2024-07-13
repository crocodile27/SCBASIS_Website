from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.hashers import make_password
import markdown

from .models import User, Courses, Competitions

# Create your views here.

ALLOWED_FILE_TYPES = []


def index(request):
    return render(request, "scbasis/index.html")


def course_guides(request):
    math_courses = Courses.objects.filter(course_category="Math").filter(viewable=True)
    english_courses = Courses.objects.filter(course_category="English").filter(
        viewable=True
    )
    science_courses = Courses.objects.filter(course_category="Science").filter(
        viewable=True
    )
    humanities_courses = Courses.objects.filter(course_category="Humanities").filter(
        viewable=True
    )
    other_courses = Courses.objects.filter(course_category="Others").filter(
        viewable=True
    )
    return render(
        request,
        "scbasis/course_guides.html",
        {
            "math_courses": math_courses,
            "english_courses": english_courses,
            "science_courses": science_courses,
            "humanities_courses": humanities_courses,
            "other_courses": other_courses,
        },
    )


def competition_guides(request):
    math_competitions = Competitions.objects.filter(competition_category="Math").filter(
        viewable=True
    )
    economic_competitions = Competitions.objects.filter(
        competition_category="Economics"
    ).filter(viewable=True)
    biology_competitions = Competitions.objects.filter(
        competition_category="Biology"
    ).filter(viewable=True)
    chemistry_competitions = Competitions.objects.filter(
        competition_category="Chemistry"
    ).filter(viewable=True)
    physics_competitions = Competitions.objects.filter(
        competition_category="Physics"
    ).filter(viewable=True)
    speech_and_debate_competition = Competitions.objects.filter(
        competition_category="Speech and Debate"
    ).filter(viewable=True)
    return render(
        request,
        "scbasis/competition_guides.html",
        {
            "math_competitions": math_competitions,
            "economic_competitions": economic_competitions,
            "biology_competitions": biology_competitions,
            "chemistry_competitions": chemistry_competitions,
            "physics_competitions": physics_competitions,
            "speech_and_debate_competitions": speech_and_debate_competition,
        },
    )


def create_guides(request):
    return render(request, "scbasis/create_guides.html")


def submit_courses(request):
    if request.method == "POST":
        name_of_course = request.POST.get("name_of_course", "")
        author = request.POST.get("author", "")
        course_description = request.FILES.get(
            "course_description"
        )  # Use .get() to avoid KeyError
        course_category = request.POST.get("course_category", "")
        url_of_image = request.POST.get("image_url", "")
        if not name_of_course or author or course_category or url_of_image:
            return render(
                request,
                "scbasis/create_guides.html",
                {
                    "error_overall_message": "Please fill in missing field/s.",
                    "name_of_course": name_of_course,
                    "author": author,
                    "course_category": course_category,
                    "url_of_image": url_of_image,
                },
            )
        if not course_description:
            return render(
                request,
                "scbasis/create_guides.html",
                {
                    "error_message": "Course description file is required.",
                    "name_of_course": name_of_course,
                    "author": author,
                    "course_category": course_category,
                    "url_of_image": url_of_image,
                },
            )

        editor = request.user
        course = Courses(
            name_of_course=name_of_course,
            author=author,
            course_description=course_description,
            editor=editor,
            course_category=course_category,
            url_of_image=url_of_image,
        )
        course.save()

        return HttpResponseRedirect(reverse("index"))

    return render(request, "scbasis/create_guides.html")


def submit_competitions(request):
    if request.method == "POST":
        name_of_competition = request.POST.get("name_of_competition", "")
        author = request.POST.get("author", "")
        competition_description = request.FILES.get(
            "competition_description"
        )  # Use .get() to avoid KeyError
        competition_category = request.POST.get("competition_category", "")
        url_of_image = request.POST.get("image_url", "")
        if not name_of_competition or author or competition_category or url_of_image:
            return render(
                request,
                "scbasis/create_guides.html",
                {
                    "error_overall_message": "Please fill in missing field/s.",
                    "name_of_competition": name_of_competition,
                    "author": author,
                    "competition_category": competition_category,
                    "url_of_image": url_of_image,
                },
            )
        if not competition_description:
            return render(
                request,
                "scbasis/create_guides.html",
                {
                    "error_message": "Competition description file is required.",
                    "name_of_competition": name_of_competition,
                    "author": author,
                    "competition_category": competition_category,
                    "url_of_image": url_of_image,
                },
            )

        editor = request.user
        competition = Competitions(
            name_of_competition=name_of_competition,
            author=author,
            competition_description=competition_description,
            editor=editor,
            competition_category=competition_category,
            url_of_image=url_of_image,
        )
        competition.save()

        return HttpResponseRedirect(reverse("index"))

    return render(request, "scbasis/create_guides.html")


def display_courses(request, course_id):
    guide = Courses.objects.get(pk=course_id)
    title = guide.course_description.read().decode("utf-8")
    course_description = markdown.markdown(title) if title else None
    return render(
        request,
        "scbasis/display_courses.html",
        {
            "guide": guide,
            "course_description": course_description,
        },
    )


def display_competitions(request, competition_id):
    guide = Competitions.objects.get(pk=competition_id)
    title = guide.competition_description.read().decode("utf-8")
    competition_description = markdown.markdown(title) if title else None
    return render(
        request,
        "scbasis/display_competitions.html",
        {
            "guide": guide,
            "competition_description": competition_description,
        },
    )


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
            return render(
                request,
                "scbasis/login.html",
                {"message": "Invalid username and/or password."},
            )
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
        hashed_password = make_password(password)
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(
                request, "scbasis/register.html", {"message": "Passwords must match."}
            )

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(
                request, "scbasis/register.html", {"message": "Username already taken."}
            )
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "scbasis/register.html")
