from django.db import models

# Create your models here.

class Topic(models.Model):

    topic_id = models.BigAutoField(auto_created=True, primary_key=True, unique=True)
    topic_name = models.CharField(max_length=255, null=True)
    
    def __str__(self) -> str:
        return self.topic_name

class Project(models.Model):

    level_choices = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    )

    project_id = models.IntegerField(auto_created=True, primary_key=True)
    project_name = models.CharField(max_length=255, null=True)
    level = models.CharField(choices=level_choices, max_length=255, null=True)
    topic_id = models.ForeignKey(Topic, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.project_name