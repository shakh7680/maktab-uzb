# Generated by Django 3.2.7 on 2021-10-05 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0004_applies_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applies',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
