# Generated by Django 5.1 on 2024-08-16 07:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_account_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='client',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.client'),
        ),
        migrations.AddField(
            model_name='withdraw',
            name='client',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.client'),
        ),
    ]
