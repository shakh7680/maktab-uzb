# Generated by Django 3.2.7 on 2021-10-07 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0005_alter_applies_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='applies',
            name='received_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='applies',
            name='recejted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]