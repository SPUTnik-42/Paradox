# Generated by Django 3.2 on 2021-06-03 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paradox', '0004_alter_user_detail_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hint',
            name='id',
        ),
        migrations.AlterField(
            model_name='hint',
            name='level',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
