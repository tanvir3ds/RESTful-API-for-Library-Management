# Generated by Django 3.0.3 on 2020-03-01 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0010_auto_20200302_0130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='department',
        ),
    ]