# Generated by Django 2.0.7 on 2018-09-25 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_post_video_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video_code_url',
            field=models.URLField(blank=True),
        ),
    ]