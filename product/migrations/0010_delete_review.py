# Generated by Django 5.1.3 on 2025-02-03 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_remove_review_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]
