# Generated by Django 3.2.5 on 2021-08-03 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_user_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
    ]