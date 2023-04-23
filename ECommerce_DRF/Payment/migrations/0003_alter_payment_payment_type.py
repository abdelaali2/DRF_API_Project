# Generated by Django 4.2 on 2023-04-23 23:01

import Payment.models
from django.db import migrations
import enumfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0002_delete_shipment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_type',
            field=enumfields.fields.EnumField(default='Credit Card', enum=Payment.models.PaymentType, max_length=11),
        ),
    ]