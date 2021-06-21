# Generated by Django 3.2.4 on 2021-06-08 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('webpages', '0002_auto_20210608_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.IntegerField(auto_created=True)),
                ('project_name', models.CharField(max_length=255, null=True)),
                ('topic_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('topic_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('topic_name', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
