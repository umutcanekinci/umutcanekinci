# Generated by Django 5.0.1 on 2024-02-14 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_project_typee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='typee',
            new_name='projectType',
        ),
    ]