from django.contrib.auth.models import User
from activityform.models import Activity
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Project, Topic
from django.shortcuts import get_object_or_404
from authentication.decorators import admin_only, ninja_only
from django.db.models import *
from django.db import connection


@login_required(login_url='login')
@admin_only
def scorecard(request):
    users = User.objects.all().exclude(id=4).exclude(id=6).order_by('first_name')
    projects = Project.objects.all().order_by('topic_id')
    topics = Topic.objects.all()

    cursor = connection.cursor()
    cursor.execute('''SELECT x.first_name, x.last_name, sum(s) as scratch , sum(c) as Circuits,sum(r) as Robotics,Sum(l) as Lego, sum(m) as Minecraft, (sum(s)+sum(c)+sum(r)+sum(l)+sum(m)) as total 
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
                        GROUP BY 1,2''')
    games = cursor.fetchall()

    data = {
        'users': users,
        'projects': projects,
        'topics': topics,
        'games': games
    }
    return render(request, 'webpages/scorecard.html', data)

@login_required(login_url='login')
def home(request):
    topics = Topic.objects.all().order_by('topic_name').exclude(topic_name__startswith='Badge').exclude(topic_name__endswith='Belt')
    return render(request, 'index.html', {'topics': topics})

@login_required(login_url='login')
def users(request):
    users = User.objects.all().exclude(id=4).exclude(id=6).order_by('first_name')
    total_users = User.objects.filter(is_superuser=False).count()
    active_users = User.objects.filter(is_active=True).filter(is_superuser=False).count()
    inactive_users = User.objects.filter(is_active=False).filter(is_superuser=False).count()

    data = {
        'users': users,
        'total': total_users,
        'active': active_users,
        'inactive': inactive_users
    }
    return render(request, 'webpages/users.html', data)

@login_required(login_url='login')
def badges(request):
    return render(request, 'webpages/badges.html')

def leaderboard(request):
    return render(request, 'webpages/leaderboard.html')

def user_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    activities = Activity.objects.filter(user_id=pk)

    data = {
        'user': user,
        'activities': activities
    }

    return render(request, 'webpages/user-profile.html', data)