# Generated by Django 3.2.4 on 2023-07-17 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0037_alter_ipaddress_geo_iso'),
    ]

    operations = [
        migrations.AddField(
            model_name='vulnerability',
            name='request',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vulnerability',
            name='response',
            field=models.TextField(blank=True, null=True),
        ),
    ]
