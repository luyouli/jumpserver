# Generated by Django 2.1 on 2018-09-03 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0020_auto_20180816_1652'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='domain',
            options={'verbose_name': 'Domain'},
        ),
        migrations.AlterModelOptions(
            name='gateway',
            options={'verbose_name': 'Gateway'},
        ),
        migrations.AlterModelOptions(
            name='node',
            options={'verbose_name': 'Node'},
        ),
    ]
