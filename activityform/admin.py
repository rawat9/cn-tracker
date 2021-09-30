from django.contrib import admin
from .resources import ActivityResource
from import_export.admin import ImportExportModelAdmin
from .models import Activity

@admin.register(Activity)
class ActivityModel(ImportExportModelAdmin):
    resource_class = ActivityResource

    list_display = ('id', 'user_id', 'project_id', 'topic_id')
    list_filter = ('date_created', 'topic_id', 'user_id')