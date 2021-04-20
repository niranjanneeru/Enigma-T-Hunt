# Generated by Django 3.1.8 on 2021-04-19 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20210419_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meme',
            name='image',
        ),
        migrations.AddField(
            model_name='meme',
            name='content',
            field=models.CharField(default='Dummy', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meme',
            name='category',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Success'), (2, 'Fail'), (3, 'Patience'), (4, 'Congratulations')], default=1),
        ),
    ]
