# Generated by Django 3.1 on 2020-08-17 00:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
