# Generated by Django 4.1.5 on 2023-02-21 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_configuration_id_alter_contract_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='contract_details',
        ),
        migrations.DeleteModel(
            name='Contract',
        ),
    ]