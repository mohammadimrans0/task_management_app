# Generated by Django 4.2.16 on 2024-11-24 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_category_tasks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='tasks',
        ),
    ]
