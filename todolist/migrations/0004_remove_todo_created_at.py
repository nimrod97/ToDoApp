# Generated by Django 3.2.6 on 2021-08-09 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_todo_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='created_at',
        ),
    ]
