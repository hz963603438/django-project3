# Generated by Django 3.2.10 on 2022-01-10 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0005_alter_node_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='node',
            options={'verbose_name': 'node list', 'verbose_name_plural': 'node'},
        ),
    ]
