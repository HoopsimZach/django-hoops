# Generated by Django 4.1.5 on 2023-02-14 01:07

from django.db import migrations, models
import main.league.config


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_contract_season_team_logo_configuration_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='gems',
        ),
        migrations.AlterField(
            model_name='configuration',
            name='settings',
            field=models.JSONField(blank=True, default=main.league.config.get_default_settings),
        ),
        migrations.AlterField(
            model_name='contract',
            name='breakdown',
            field=models.JSONField(blank=True, default=main.league.config.get_default_contract),
        ),
        migrations.AlterField(
            model_name='featurelist',
            name='features',
            field=models.JSONField(blank=True, default=main.league.config.get_default_features),
        ),
        migrations.AlterField(
            model_name='historylist',
            name='history',
            field=models.JSONField(blank=True, default=main.league.config.get_default_history),
        ),
    ]