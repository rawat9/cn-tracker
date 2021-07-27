from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from .models import Activity
from webpages.models import Project, Topic

# Create your views here.

def activity_form(request):

    if request.method == 'POST':
        user_id = request.POST['user_id']
        topic_id = request.POST['topic_id']
        project_id = request.POST['project_id']
        rating = request.POST['rating']
        sensei_name = request.POST['sensei_name']
        comment = request.POST['comment']

        if Activity.objects.filter(user_id=user_id).filter(project_id=project_id).exists():
            messages.warning(request, 'Record already exists')
            return redirect('scorecard')
        else:
            activity_form = Activity(user_id=User.objects.get(id=user_id), 
                            topic_id=Topic.objects.get(topic_id=topic_id),
                            project_id=Project.objects.get(project_id=project_id), 
                            rating=rating, 
                            sensei_name=sensei_name, 
                            comment=comment)
            activity_form.save()
            messages.success(request, 'Record Saved Successfully!')
            return redirect('scorecard')