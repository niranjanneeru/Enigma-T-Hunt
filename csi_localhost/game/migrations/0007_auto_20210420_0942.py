# Generated by Django 3.1.8 on 2021-04-20 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_auto_20210420_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='number',
            field=models.PositiveSmallIntegerField(unique=True),
        ),
    ]
