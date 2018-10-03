# Generated by Django 2.1 on 2018-10-03 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20181002_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='competitionrecord',
            name='registered',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='guestlecturerecord',
            name='registered',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='seminarrecord',
            name='registered',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='trainingrecord',
            name='registered',
            field=models.IntegerField(default=0),
        ),
    ]
