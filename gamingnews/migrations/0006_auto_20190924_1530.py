# Generated by Django 2.2.3 on 2019-09-24 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamingnews', '0005_auto_20190924_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='description',
            field=models.TextField(),
        ),
    ]
