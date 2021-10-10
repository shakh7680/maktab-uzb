# Generated by Django 3.2.7 on 2021-10-04 21:22

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(blank=True, storage=django.core.files.storage.FileSystemStorage(location='/media/profile_photos'), upload_to=''),
        ),
    ]
