from django.db import models
from django.contrib.auth.models import User
from webpages.models import Project, Topic

# Create your models here.

class Activity(models.Model):
	SENSEIS = (
		('Anurag Rawat', 'Anurag Rawat'),
		('Siddhant Dalal', 'Siddhant Dalal'),
		('Manan Adhvaryu', 'Manan Adharvyu'),
		('Marta Garcia', 'Marta Garcia'),	
		('Omar Veiga', 'Omar Veiga'), 
		('Simran Tulsiani', 'Simran Tulsiani'),
		('Ilham Esse', 'Ilham Esse'),
		('Istabraq Ahmed', 'Istrabraq Ahmed'),
		('Kyan Ung', 'Kyan Ung'),
		('Ayman El Behri', 'Ayman El Behri'),
	)

	user_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	topic_id = models.ForeignKey(Topic, null=True, on_delete=models.SET_NULL)
	project_id = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL)
	rating = models.IntegerField(null=True)
	sensei_name = models.CharField(choices=SENSEIS, max_length=255, null=True)
	completion_percentage = models.IntegerField(default=100)
	comment = models.TextField(blank=True)
	date_created = models.DateTimeField(null=True)

	class Meta:
		verbose_name_plural = "Activities"

	def __str__(self) -> str:
		return self.user_id.first_name + ' ' + self.user_id.last_name