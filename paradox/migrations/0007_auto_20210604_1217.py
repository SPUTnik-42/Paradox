# Generated by Django 3.2 on 2021-06-04 06:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paradox', '0006_auto_20210603_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='team_member',
            name='level',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team_member',
            name='beta',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='beta', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='team_member',
            name='gamma',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='gamma', to=settings.AUTH_USER_MODEL),
        ),
    ]
