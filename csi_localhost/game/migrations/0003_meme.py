# Generated by Django 3.1.8 on 2021-04-19 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20210419_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='meme_pics/')),
                ('category', models.PositiveSmallIntegerField(choices=[('Success', 1), ('Fail', 2)], default=1)),
            ],
        ),
    ]