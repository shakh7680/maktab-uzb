# Generated by Django 3.2.7 on 2021-10-05 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schools', '0003_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='applies',
            name='user',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, to='accounts.user'),
            preserve_default=False,
        ),
    ]
