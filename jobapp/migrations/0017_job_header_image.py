# Generated by Django 3.2.5 on 2021-07-29 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0016_alter_job_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
