from django.contrib import admin
from django.contrib.auth import models
from .models import Activity

# Register your models here.
class ActivityModel(admin.ModelAdmin):
	object_name = 'Activity'
	list_display = ('id', 'user_id', 'project_id','topic_id')
	list_filter = ('date_created', 'topic_id',)

admin.site.register(Activity, ActivityModel)