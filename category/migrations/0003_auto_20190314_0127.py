# Generated by Django 2.1 on 2019-03-13 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20190314_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='Slug'),
        ),
    ]