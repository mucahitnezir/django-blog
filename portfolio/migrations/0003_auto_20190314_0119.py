# Generated by Django 2.1 on 2019-03-13 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20190314_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Slug'),
        ),
    ]
