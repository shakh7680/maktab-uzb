# Generated by Django 3.2.7 on 2021-10-05 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]
