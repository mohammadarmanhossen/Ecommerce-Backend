# Generated by Django 5.1.3 on 2025-01-26 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_product_created_at_remove_product_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='product/'),
        ),
    ]
