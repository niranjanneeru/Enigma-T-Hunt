# Generated by Django 3.1.8 on 2021-04-20 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('response', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='create_date',
            field=models.DateTimeField(),
        ),
    ]
