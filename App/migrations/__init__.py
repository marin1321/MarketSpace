# Generated by Django 3.2.6 on 2021-09-07 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_auto_20210907_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='numero',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
