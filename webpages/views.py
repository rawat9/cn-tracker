from datetime import datetime
from django.contrib.auth.models import User, Group
from django.db.models.functions import Concat, Lower, Cast
from django.contrib import messages
from django.http import HttpResponse
from activityform.models import Activity
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Topic
from authentication.decorators import admin_only
from django.db.models import DateField, Value as V, Case, When
from django.db import connection
import xlwt


@login_required(login_url="login")
@admin_only
def scorecard(request):
    users = User.objects.all().exclude(id=4).exclude(id=6).order_by("first_name")
    projects = Project.objects.all().order_by("topic_id")
    topics = Topic.objects.all()

    cursor = connection.cursor()
    cursor.execute(
        """SELECT x.first_name, x.last_name, sum(s) as scratch , sum(c) as Circuits,sum(r) as Robotics,Sum(l) as Lego, sum(m) as Minecraft, (sum(s)+sum(c)+sum(r)+sum(l)+sum(m)) as total 
                    FROM 
                    (SELECT first_name , last_name , topic_id_id , 
                    CASE 
                        WHEN topic_id_id=1 OR topic_id_id=7 OR topic_id_id=8 OR topic_id_id=10 THEN count(project_id_id) else 0 END as s,
                    CASE 
                        WHEN topic_id_id=2 THEN count(project_id_id) else 0 END as c,
                    CASE 
                        WHEN topic_id_id=3 THEN count(project_id_id) else 0 END as r,
                    CASE 
                        WHEN topic_id_id=4 THEN count(project_id_id) else 0 END as l,
                    CASE
                        WHEN topic_id_id=9 THEN count(project_id_id) else 0 END as m
                        FROM activityform_activity a 
                        INNER JOIN auth_user au on au.id = a.user_id_id 
                        GROUP by 1,2,3)x 
                        GROUP BY 1,2"""
    )
    games = cursor.fetchall()

    data = {"users": users, "projects": projects, "topics": topics, "games": games}
    return render(request, "webpages/scorecard.html", data)


@login_required(login_url="login")
def home(request):
    topics = (
        Topic.objects.all()
        .order_by("topic_name")
        .exclude(topic_name__startswith="Badge")
        .exclude(topic_name__endswith="Belt")
    )
    return render(request, "index.html", {"topics": topics})


def add_user(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        username = f"{firstname.strip().lower()}{lastname.strip().lower()}n12"

        if User.objects.filter(username=username).exists():
            messages.warning(request, "User already exists")
            return redirect("users")
        else:
            new_user = User.objects.create_user(
                first_name=firstname.title(),
                last_name=lastname.title(),
                username=username,
                password="ninjan12",
            )
            new_user.save()
            group = Group.objects.get(name="ninja")
            new_user.groups.add(group)

            messages.success(request, "User successfully created!")
            return redirect("users")


def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, "webpages/edit-user.html", {"user": user})


def update_user(request, pk):
    user = get_object_or_404(User, pk=pk)

    user.first_name = request.POST["firstname"]
    user.last_name = request.POST["lastname"]
    user.is_active = request.POST.get("status", "") == "on"
    user.username = (
        f"{user.first_name.strip().lower()}{user.last_name.strip().lower()}n12"
    )
    user.save()
    messages.success(request, "User updated successfully!")
    return redirect("users")


@login_required(login_url="login")
def users(request):
    users = User.objects.filter(groups__name="ninja").order_by("first_name")
    total_users = User.objects.filter(groups__name="ninja").count()
    active_users = User.objects.filter(groups__name="ninja", is_active=True).count()
    inactive_users = User.objects.filter(groups__name="ninja", is_active=False).count()

    data = {
        "users": users,
        "total": total_users,
        "active": active_users,
        "inactive": inactive_users,
    }
    return render(request, "webpages/users.html", data)


@login_required(login_url="login")
def badges(request):
    return render(request, "webpages/badges.html")


@login_required(login_url="login")
def leaderboard(request):
    return render(request, "webpages/leaderboard.html")


@login_required(login_url="login")
def user_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    activities = Activity.objects.filter(user_id=pk).order_by("-date_created")

    data = {
        "user": user,
        "activities": activities,
    }

    return render(request, "webpages/user-profile.html", data)


def export_excel(request):
    response = HttpResponse(content_type="application/ms-excel")
    response["Content-Disposition"] = (
        "attachment; filename=User"
        + "-"
        + datetime.today().strftime("%b-%d-%Y")
        + ".xls"
    )

    wb = xlwt.Workbook(encoding="utf-8")
    ws = wb.add_sheet("Users")
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = [
        "Firstname",
        "Lastname",
        "Username",
        "Dojo Username",
        "Status",
        "Date Joined",
    ]

    for col in range(len(columns)):
        ws.write(0, col, columns[col], font_style)

    font_style = xlwt.XFStyle()

    rows = (
        User.objects.filter(groups__name="ninja")
        .order_by("first_name")
        .values_list("first_name", "last_name", "username")
        .annotate(
            dojo_username=Concat(Lower("first_name"), V("."), Lower("last_name")),
            status=Case(
                When(is_active=True, then=V("Active")),
                When(is_active=False, then=V("Inactive")),
            ),
            date=Cast("date_joined", output_field=DateField()),
        )
    )

    row = 0
    for data in rows:
        row += 1

        for col in range(len(data)):
            ws.write(row, col, str(data[col]), font_style)

    wb.save(response)
    return response


def error_404(request, exception):
    return render(request, "error/error_404.html")


def error_500(request):
    return render(request, "error/error_500.html")
