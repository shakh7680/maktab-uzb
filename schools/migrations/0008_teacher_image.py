# Generated by Django 3.2.7 on 2021-10-07 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0007_rename_recejted_at_applies_rejected_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, upload_to='teachers/%Y/%m/%d'),
        ),
    ]