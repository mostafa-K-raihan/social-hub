# Generated by Django 2.2.4 on 2019-08-23 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_convert_to_utf8mb4'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='requestId',
        ),
    ]