# Generated by Django 3.2.7 on 2021-10-02 10:54

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('body', models.TextField()),
                ('region', models.CharField(max_length=50)),
                ('school', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='applicants/%Y/%m/%d')),
                ('status', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolname', models.CharField(max_length=60)),
                ('region', models.CharField(max_length=3, null=True)),
                ('school_type', models.CharField(max_length=3, null=True)),
                ('schoolnumber', models.IntegerField()),
                ('adress', models.CharField(max_length=70)),
                ('teachersnumber', models.IntegerField()),
                ('pupilsnumber', models.IntegerField()),
                ('website', models.CharField(max_length=100, unique=True)),
                ('photo_main', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('achievments', models.TextField(blank=True)),
                ('school_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.schools', verbose_name='School of Student')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('role', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)])),
                ('ranking', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('school_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.schools', verbose_name='School of Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=50)),
                ('subject_credit', models.IntegerField()),
                ('student_id', models.ManyToManyField(related_name='student', to='schools.Student')),
                ('teacher_id', models.ManyToManyField(related_name='teacher', to='schools.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.teacher', verbose_name='Comments for teacher')),
            ],
        ),
    ]
