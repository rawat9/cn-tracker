# Generated by Django 4.0.1 on 2022-05-21 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activityform', '0029_remove_activity_rating_alter_activity_sensei_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='laptop_num',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
