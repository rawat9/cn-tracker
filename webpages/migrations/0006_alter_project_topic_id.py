# Generated by Django 3.2.4 on 2021-06-15 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0005_auto_20210611_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='topic_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webpages.topic'),
        ),
    ]
