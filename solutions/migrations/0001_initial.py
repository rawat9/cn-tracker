# Generated by Django 4.0.1 on 2022-04-02 20:58

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('webpages', '0006_alter_project_topic_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('question_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('notes', ckeditor.fields.RichTextField(null=True)),
                ('solution', ckeditor.fields.RichTextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('project_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webpages.project')),
                ('topic_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webpages.topic')),
            ],
        ),
    ]
