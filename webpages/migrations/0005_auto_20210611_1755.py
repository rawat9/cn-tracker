# Generated by Django 3.2.4 on 2021-06-11 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0004_auto_20210609_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='topic_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='webpages.topic'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='topic_id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True),
        ),
    ]
