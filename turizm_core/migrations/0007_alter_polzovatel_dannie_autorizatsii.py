# Generated by Django 5.1.4 on 2025-01-29 21:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turizm_core', '0006_alter_polzovatel_dannie_autorizatsii'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polzovatel',
            name='dannie_autorizatsii',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
