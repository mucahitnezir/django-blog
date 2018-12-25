# Generated by Django 2.1 on 2018-11-22 21:31

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Category Name')),
                ('slug', models.SlugField(editable=False, unique=True, verbose_name='Slug')),
                ('type', models.CharField(choices=[('post', 'Post Category'), ('portfolio', 'Portfolio Category'), ('service', 'Service Category')], default='post', max_length=9, verbose_name='Category Type')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Category Description')),
                ('meta_description', models.TextField(blank=True, null=True, verbose_name='Meta Description')),
                ('published_at', models.DateTimeField(auto_now_add=True, verbose_name='Publishing Date')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'categories',
                'ordering': ['name'],
            },
        ),
    ]
