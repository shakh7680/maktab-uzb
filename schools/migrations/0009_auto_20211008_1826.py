# Generated by Django 3.2.7 on 2021-10-08 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0008_teacher_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schools',
            name='photo_1',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='schools',
            name='photo_2',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='schools',
            name='photo_3',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='schools',
            name='photo_main',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
