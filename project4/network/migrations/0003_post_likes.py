# Generated by Django 4.2.5 on 2023-10-05 21:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_alter_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='postLikes', to=settings.AUTH_USER_MODEL),
        ),
    ]
