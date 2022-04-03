from django.contrib import admin
from solutions.models import Solution

# Register your models here.

@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ('question_id', 'question_title', 'topic_id', 'project_id')