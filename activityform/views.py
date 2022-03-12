from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import Activity
from webpages.models import Project, Topic


def activity_form(request):

    if request.method == "POST":
        user_id = request.POST["user_id"]
        topic_id = request.POST["topic_id"]
        project_id = request.POST["project_id"]
        date_created = request.POST["date_created"]
        sensei_name = request.POST["sensei_name"]
        ninja_comment = request.POST["ninja_comment"]
        is_completed = request.POST.get("is_completed", "") == "on"

        if Activity.objects.filter(
            user_id=user_id, project_id=project_id, is_completed=True
        ).exclude(topic_id=21).exists():
            messages.warning(request, "Record Already Exists")
            return redirect("activity")
        else:
            activity_form = Activity(
                user_id=User.objects.get(id=user_id),
                topic_id=Topic.objects.get(topic_id=topic_id),
                project_id=Project.objects.get(project_id=project_id),
                date_created=date_created,
                sensei_name=sensei_name,
                ninja_comment=ninja_comment,
                is_completed=is_completed,
            )

            activity_form.save()
            messages.success(request, "Record Saved Successfully!")
            return redirect("activity")


@login_required(login_url="login")
def act(request):
    users = User.objects.all().exclude(id=4).exclude(id=6).order_by("first_name")
    projects = Project.objects.all().order_by("topic_id")
    topics = Topic.objects.all()
    senseis = User.objects.filter(is_superuser=True).exclude(id=72)

    data = {"users": users, "projects": projects, "topics": topics, "senseis": senseis}
    return render(request, "webpages/activityform.html", data)


def load_projects(request):
    topic_id = request.GET.get("topic_id")
    projects = Project.objects.filter(topic_id=topic_id)
    return render(request, "webpages/options.html", {"projects": projects})
