# Generated by Django 4.2.2 on 2023-06-25 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1990-8-6'),
            preserve_default=False,
        ),
    ]
