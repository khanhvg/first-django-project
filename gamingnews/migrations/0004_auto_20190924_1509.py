# Generated by Django 2.2.3 on 2019-09-24 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamingnews', '0003_auto_20190924_1507'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='games',
            options={},
        ),
        migrations.AlterIndexTogether(
            name='games',
            index_together=set(),
        ),
        migrations.RemoveField(
            model_name='games',
            name='slug',
        ),
    ]
