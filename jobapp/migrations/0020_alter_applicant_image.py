# Generated by Django 3.2.5 on 2021-08-03 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobapp', '0019_applicant_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Applicant', to=settings.AUTH_USER_MODEL),
        ),
    ]
