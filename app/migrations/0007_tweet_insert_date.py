# Generated by Django 2.2.4 on 2019-08-23 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_tweet_requestid'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='insert_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]