# Generated by Django 2.1 on 2018-11-22 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='phone_number',
        ),
    ]