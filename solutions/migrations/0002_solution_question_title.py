# Generated by Django 4.0.1 on 2022-04-03 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='question_title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
