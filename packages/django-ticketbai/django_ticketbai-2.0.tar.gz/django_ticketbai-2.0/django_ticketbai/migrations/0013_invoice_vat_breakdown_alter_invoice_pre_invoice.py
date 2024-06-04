# Generated by Django 4.1.6 on 2023-07-28 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("django_ticketbai", "0012_invoice_pre_invoice_alter_invoice_signature_value"),
    ]

    operations = [
        migrations.AddField(
            model_name="invoice",
            name="vat_breakdown",
            field=models.TextField(default=[], verbose_name="VAT breakdown"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="invoice",
            name="pre_invoice",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="django_ticketbai.invoice",
                verbose_name="Previous invoice",
            ),
        ),
    ]
