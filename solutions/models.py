from django.db import models
from ckeditor.fields import RichTextField
from webpages.models import Project, Topic

# Create your models here.

class Solution(models.Model):
	topic_id = models.ForeignKey(Topic, null=True, on_delete=models.SET_NULL)
	project_id = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL)
	question_id = models.BigAutoField(primary_key=True, unique=True, auto_created=True)
	question_title = models.CharField(max_length=255, null=True)
	notes = RichTextField(null=True, blank=True)
	solution = RichTextField(config_name='special')
	date_created = models.DateTimeField(auto_now_add=True)
