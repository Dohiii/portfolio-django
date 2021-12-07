from django.shortcuts import get_object_or_404, render

from .models import Project


def get_date(post):
    return post["date"]


def index(request):
    project_dict = Project.objects.all().order_by('-date')[:3]
    return render(request, "portfolio/index.html", {
        "projects": project_dict
    })


def projecty(request):
    project_dict = Project.objects.all()
    return render(request, "portfolio/projecty.html", {
        "projects": project_dict
    })


def contact(request):
    return render(request, "portfolio/contact.html")


def project_detail(request, slug):
    # post_dict = Post.objects.get(slug=slug)
    project_dict = get_object_or_404(Project, slug=slug)

    return render(request, "portfolio/project-detail.html", {
        "project": project_dict,
    })
