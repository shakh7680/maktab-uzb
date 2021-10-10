# Generated by Django 3.2.7 on 2021-10-02 10:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_of_subject', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(11)])),
                ('subject', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=100)),
                ('isbn', models.IntegerField()),
                ('edition', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(11)])),
                ('photo', models.ImageField(blank=True, upload_to='subjects/%Y/%m/%d')),
                ('file', models.FileField(upload_to='subjects/%Y/%m/%d')),
            ],
        ),
    ]