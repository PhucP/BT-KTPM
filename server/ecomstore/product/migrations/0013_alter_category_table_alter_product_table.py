# Generated by Django 4.1.6 on 2023-02-28 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_alter_product_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
        migrations.AlterModelTable(
            name='product',
            table='product',
        ),
    ]
