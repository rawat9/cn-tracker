from django.contrib import admin
from .resources import ProjectResource
from import_export.admin import ImportExportModelAdmin
from .models import Project, Topic

@admin.register(Project)
class ProjectAdmin(ImportExportModelAdmin):
    resource_class = ProjectResource
    
    list_display = ('project_id', 'project_name', 'topic_id', 'level')
    list_filter = ('topic_id',)

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('topic_id', 'topic_name')