# Generated by Django 2.2 on 2019-04-15 06:04

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20181226_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventrecord',
            name='content',
            field=froala_editor.fields.FroalaField(default=''),
            preserve_default=False,
        ),
    ]
