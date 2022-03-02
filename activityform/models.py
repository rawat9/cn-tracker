from django.db import models
from django.contrib.auth.models import User
from webpages.models import Project, Topic

class Activity(models.Model):
	user_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	topic_id = models.ForeignKey(Topic, null=True, on_delete=models.SET_NULL)
	project_id = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL)
	sensei_name = models.CharField(max_length=255, null=True)
	is_completed = models.BooleanField()
	ninja_comment = models.TextField(blank=True)
	sensei_comment = models.TextField(blank=True)
	date_created = models.DateField(null=True)

	class Meta:
		verbose_name_plural = "Activities"

	def __str__(self) -> str:
		return self.user_id.first_name + ' ' + self.user_id.last_name
