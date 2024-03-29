# Generated by Django 2.2.3 on 2019-09-24 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamingnews', '0002_auto_20190924_1503'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='games',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='games',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
        migrations.AlterIndexTogether(
            name='games',
            index_together={('id', 'slug')},
        ),
    ]
