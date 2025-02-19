# Generated by Django 5.1.3 on 2025-02-18 16:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_remove_checkout_order_remove_checkout_total_amount_and_more'),
        ('product', '0029_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('start_date', models.DateField()),
                ('out_date', models.DateField()),
                ('is_paid', models.BooleanField(default=False)),
                ('total_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.cart')),
            ],
        ),
        migrations.DeleteModel(
            name='Checkout',
        ),
    ]
