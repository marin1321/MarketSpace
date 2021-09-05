# Generated by Django 3.2.6 on 2021-09-03 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '0003_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='usuario',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET, to='auth.user'),
            preserve_default=False,
        ),
    ]
