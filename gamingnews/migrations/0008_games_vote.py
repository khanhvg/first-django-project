# Generated by Django 2.2.3 on 2019-09-24 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamingnews', '0007_auto_20190924_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='vote',
            field=models.FloatField(null=True),
        ),
    ]
