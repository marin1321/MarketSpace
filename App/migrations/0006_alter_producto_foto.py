# Generated by Django 3.2.6 on 2021-09-04 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_auto_20210904_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='foto',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
    ]
