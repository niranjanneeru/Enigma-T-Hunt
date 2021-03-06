# Generated by Django 3.1.8 on 2021-04-20 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_auto_20210420_0942'),
        ('user_profile', '0007_profile_has_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='current_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.question'),
        ),
    ]
