from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import Activity
from webpages.models import Project, Topic

# Create your views here.

def activity_form(request):

    if request.method == 'POST':
        user_id = request.POST['user_id']
        topic_id = request.POST['topic_id']
        project_id = request.POST['project_id']
        date_created = request.POST['date_created']
        ninja_comment = request.POST['ninja_comment']
        is_completed = request.POST.get('is_completed', '') == 'on'

        activity_form = Activity(user_id=User.objects.get(id=user_id), 
                        topic_id=Topic.objects.get(topic_id=topic_id),
                        project_id=Project.objects.get(project_id=project_id), 
                        date_created=date_created, 
                        ninja_comment=ninja_comment,
                        is_completed=is_completed)

        activity_form.save()
        messages.success(request, 'Record Saved Successfully!')
        return redirect('activity')

@login_required(login_url='login')
def act(request):
    users = User.objects.all().exclude(id=4).exclude(id=6).order_by('first_name')
    projects = Project.objects.all().order_by('topic_id')
    topics = Topic.objects.all()
    senseis = User.objects.filter(is_superuser=True).exclude(user_id=72)

    data = {
        'users': users,
        'projects': projects,
        'topics': topics,
        'senseis': senseis
    }
    return render(request, 'webpages/activityform.html', data)

def load_projects(request):
    topic_id = request.GET.get('topic_id')
    projects = Project.objects.filter(topic_id=topic_id)
    return render(request, 'webpages/options.html', {'projects': projects})
