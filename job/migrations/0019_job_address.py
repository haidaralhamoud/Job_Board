# Generated by Django 3.2.7 on 2022-08-05 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0018_remove_job_fav_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='address',
            field=models.CharField(default='unknown', max_length=100),
        ),
    ]
