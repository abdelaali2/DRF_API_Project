# Generated by Django 4.2 on 2023-04-23 22:38

import Payment.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cart', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', enumfields.fields.EnumField(default='Credit Card', enum=Payment.models.PaymentType, max_length=10)),
                ('card_number', models.CharField(blank=True, max_length=16)),
                ('expiration_month', models.CharField(blank=True, max_length=2)),
                ('expiration_year', models.CharField(blank=True, max_length=4)),
                ('cvv', models.CharField(blank=True, max_length=4)),
                ('iban', models.CharField(blank=True, max_length=34)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cart.cart')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Payment.payment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]