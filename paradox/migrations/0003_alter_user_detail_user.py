# Generated by Django 3.2 on 2021-06-03 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paradox', '0002_delete_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_detail',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
