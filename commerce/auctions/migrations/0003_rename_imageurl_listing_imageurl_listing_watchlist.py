# Generated by Django 4.2.5 on 2023-09-15 20:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_category_listing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='imageUrl',
            new_name='imageurl',
        ),
        migrations.AddField(
            model_name='listing',
            name='watchlist',
            field=models.ManyToManyField(blank=True, null=True, related_name='listingWatchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]