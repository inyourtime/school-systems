from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePage, name="home-page"),
    path("about/", views.AboutPage, name="about-page"),
    path("contact/", views.ContactUs, name="contact-page"),
    path("score/", views.ShowScore, name="score-page"),
    path("register/", views.Register, name="register-page"),
]
