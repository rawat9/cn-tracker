# Generated by Django 3.2.4 on 2021-06-13 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activityform', '0013_auto_20210613_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='sensei_name',
            field=models.CharField(choices=[('Anurag Rawat', 'Anurag Rawat'), ('Elena Bardho', 'Elena Bardho'), ('Goundo Sidibe', 'Goundo Sidibe'), ('Siddhant Dalal', 'Siddhant Dalal'), ('Manan Adhvaryu', 'Manan Adharvyu'), ('Leonie Dennett', 'Leonie Dennett')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
