from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING, SET_NULL
from webpages.models import Project, Topic

# Create your models here.

class Activity(models.Model):
	SENSEIS = (
		('Anurag Rawat', 'Anurag Rawat'),
		('Leonie Dennett', 'Leonie Dennett'),
		('Elena Bardho', 'Elena Bardho'),
		('Goundo Sidibe', 'Goundo Sidibe'),
		('Siddhant Dalal', 'Siddhant Dalal'),
		('Manan Adhvaryu', 'Manan Adharvyu'),
		('Marta Garcia', 'Marta Garcia'),	
		('Omar Veiga', 'Omar Veiga'), 
		('Simran Tulsiani', 'Simran Tulsiani'),
		('Ilham Esse', 'Ilham Esse'),
		('Istabraq Ahmed', 'Istrabraq Ahmed'),
		('Manali Ballewar', 'Manali Ballewar'),
		('Polly Thomas', 'Polly Thomas')
	)

	user_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	topic_id = models.ForeignKey(Topic, null=True, on_delete=models.SET_NULL)
	project_id = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL)
	rating = models.IntegerField(null=True)
	sensei_name = models.CharField(choices=SENSEIS, max_length=255, null=True)
	completion_percentage = models.IntegerField(default=100)
	comment = models.TextField(blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	class Meta:
		verbose_name_plural = "Activities"

	def __str__(self) -> str:
		return self.user_id.first_name + ' ' + self.user_id.last_name