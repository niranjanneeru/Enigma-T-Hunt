# Generated by Django 3.1.8 on 2021-04-20 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rules',
            options={'verbose_name': 'Rule', 'verbose_name_plural': 'Rules'},
        ),
    ]