# Generated by Django 3.1.8 on 2021-04-19 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_auto_20210419_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='marks',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]