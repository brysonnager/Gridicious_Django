# Generated by Django 4.0 on 2021-12-18 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='player_name',
            field=models.CharField(default='bdog', max_length=15),
            preserve_default=False,
        ),
    ]
