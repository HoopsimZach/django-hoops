# Generated by Django 4.1.5 on 2023-05-29 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0054_discorduser_player_slots'),
    ]

    operations = [
        migrations.AddField(
            model_name='discorduser',
            name='auto_collect_rewards',
            field=models.BooleanField(default=False),
        ),
    ]