# Generated by Django 4.0.1 on 2022-01-21 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activityform', '0027_alter_activity_is_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='sensei_name',
            field=models.CharField(choices=[('Anurag Rawat', 'Anurag Rawat'), ('Siddhant Dalal', 'Siddhant Dalal'), ('Marta Garcia', 'Marta Garcia'), ('Omar Veiga', 'Omar Veiga'), ('Simran Tulsiani', 'Simran Tulsiani'), ('Ilham Esse', 'Ilham Esse'), ('Kyan Ung', 'Kyan Ung'), ('Ayman El Behri', 'Ayman El Behri'), ('Amber Barakat', 'Amber Barakat'), ('Devarsh Patel', 'Devarsh Patel'), ('Rushabh Rana', 'Rushabh Rana')], max_length=255, null=True),
        ),
    ]
