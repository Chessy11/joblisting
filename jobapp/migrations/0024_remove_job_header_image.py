# Generated by Django 3.2.5 on 2021-08-04 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0023_remove_applicant_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='header_image',
        ),
    ]
