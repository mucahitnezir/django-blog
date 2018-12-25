# Generated by Django 2.1 on 2018-11-22 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(editable=False, max_length=32, unique=True, verbose_name='Parameter')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Parameter Description')),
                ('value', models.TextField(blank=True, null=True, verbose_name='Parameter Value')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Last Updated Date')),
            ],
            options={
                'verbose_name': 'Parameter',
                'verbose_name_plural': 'Parameters',
                'db_table': 'settings',
                'ordering': ['key'],
            },
        ),
    ]
