# Generated by Django 5.1.3 on 2025-02-19 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_order_delete_checkout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='out_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='start_date',
        ),
    ]
