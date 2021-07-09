from django.contrib.auth.models import User
from activityform.models import Activity
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Project, Topic
from authentication.decorators import admin_only, ninja_only
from django.db.models import *
from django.db import connection


@login_required(login_url='login')
@ninja_only
def dashboard(request, pk):

    total = Project.objects.all().count()

    # Completed Projects - count()    
    scratch_completed = Activity.objects.filter(user_id=pk).filter(topic_id=1).count()
    circuits_completed = Activity.objects.filter(user_id=pk).filter(topic_id=2).count()
    robotics_completed = Activity.objects.filter(user_id=pk).filter(topic_id=3).count()
    lego_completed = Activity.objects.filter(user_id=pk).filter(topic_id=4).count()
    typing_completed = Activity.objects.filter(user_id=pk).filter(topic_id=5).count()

    scratch_total = Project.objects.filter(topic_id=1).count()
    circuits_total = Project.objects.filter(topic_id=2).count()
    robotics_total = Project.objects.filter(topic_id=3).count()
    lego_total = Project.objects.filter(topic_id=4).count()
    typing_total = Project.objects.filter(topic_id=5).count()

    # Completion Percentage 
    scratch_completion = int((scratch_completed / scratch_total) * 100)
    circuits_completion = int((circuits_completed / 10) * 100)
    robotics_completion = int((robotics_completed / robotics_total) * 100)
    lego_completion = int((lego_completed / lego_total) * 100)
    # typing_completion = int((typing_completed / typing_total) * 100)
    
    all_completed = [scratch_completed, circuits_completed, robotics_completed, lego_completed, typing_completed]

    data = {
        'scratch_completion': scratch_completion,
        'circuits_completion': circuits_completion,
        'robotics_completion': robotics_completion,
        'lego_completion': lego_completion,
        'circuits_total': circuits_total,
        'robotics_total': robotics_total,
        'lego_total': lego_total,
        'typing_total': typing_total,
        'all_completed': all_completed,
        'total': total,
    }
    return render(request, 'webpages/dashboard.html', data)

@login_required(login_url='login')
@admin_only
def scorecard(request):
    users = User.objects.all().exclude(id=4).exclude(id=6).order_by('first_name')
    projects = Project.objects.all().order_by('topic_id')
    topics = Topic.objects.all()

    cursor = connection.cursor()
    cursor.execute('''SELECT x.first_name, x.last_name, sum(s) as scratch , sum(c) as Circuits,sum(r) as Robotics,Sum(l) as Lego, (sum(s)+sum(c)+sum(r)+sum(l)) as total 
                    FROM 
                    (SELECT first_name , last_name , topic_id_id , 
                    CASE 
                        WHEN topic_id_id=1 OR topic_id_id=7 OR topic_id_id=8 THEN count(project_id_id) else 0 END as s,
                    CASE 
                        WHEN topic_id_id=2 THEN count(project_id_id) else 0 END as c,
                    CASE 
                        WHEN topic_id_id=3 THEN count(project_id_id) else 0 END as r,
                    CASE 
                        WHEN topic_id_id=4 THEN count(project_id_id) else 0 END as l 
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

def scratch(request, pk):  
    students = Activity.objects.filter(user_id=pk).order_by('-date_created').filter(topic_id=1)
    data = {
        'students': students,
    }
    return render(request, 'webpages/scratch.html', data)

def circuits(request, pk):
    students = Activity.objects.filter(user_id=pk).order_by('-date_created').filter(topic_id=2)
    data = {
        'students': students,
    }
    return render(request, 'webpages/circuits.html', data)

def artek(request, pk):
    students = Activity.objects.filter(user_id=pk).order_by('-date_created').filter(topic_id=3)
    data = {
        'students': students,
    }
    return render(request, 'webpages/artek.html', data)

def lego(request, pk):
    students = Activity.objects.filter(user_id=pk).order_by('-date_created').filter(topic_id=4)
    data = {
        'students': students,
    }
    return render(request, 'webpages/lego.html', data)

def typing(request, pk):
    students = Activity.objects.filter(user_id=pk).order_by('-date_created').filter(topic_id=5)
    data = {
        'students': students,
    }
    return render(request, 'webpages/typing.html', data)