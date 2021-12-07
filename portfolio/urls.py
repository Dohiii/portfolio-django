from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("projecty", views.projecty, name='projecty'),
    path("contact", views.contact, name='contact'),
    # posts/something - called slug!
    path("projecty/<slug:slug>", views.project_detail, name='project-detail-page'),
]
