# Generated by Django 3.2.4 on 2021-06-13 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activityform', '0015_rename_user_id_activity_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='user',
            new_name='user_id',
        ),
    ]
