# Generated by Django 5.0.4 on 2024-04-30 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quality_control', '0002_alter_bugreport_priority_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featurerquest',
            name='project',
        ),
    ]
