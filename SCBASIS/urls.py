from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_guides", views.create_guides, name="create_guides"),
    path("course_guides", views.course_guides, name="course_guides"),
    path("competition_guides", views.competition_guides, name="competition_guides"),
    path("submit_courses", views.submit_courses, name="submit_courses"),
    path("submit_competitions", views.submit_competitions, name="submit_competitions"),
    path(
        "<int:course_id>/display_courses", views.display_courses, name="display_courses"
    ),
    path(
        "<int:competition_id>/display_competitions",
        views.display_competitions,
        name="display_competitions",
    ),
]
