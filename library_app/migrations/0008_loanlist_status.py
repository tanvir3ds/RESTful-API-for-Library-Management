# Generated by Django 3.0.3 on 2020-03-01 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0007_auto_20200302_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanlist',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
