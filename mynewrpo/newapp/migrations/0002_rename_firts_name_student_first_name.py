# Generated by Django 4.0.5 on 2022-06-30 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='firts_name',
            new_name='first_name',
        ),
    ]
