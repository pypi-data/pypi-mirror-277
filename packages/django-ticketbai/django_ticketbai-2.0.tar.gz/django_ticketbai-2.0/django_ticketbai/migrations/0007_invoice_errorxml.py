# Generated by Django 4.1.6 on 2023-07-07 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("django_ticketbai", "0006_config_is_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="invoice",
            name="errorxml",
            field=models.TextField(blank=True, null=True),
        ),
    ]
