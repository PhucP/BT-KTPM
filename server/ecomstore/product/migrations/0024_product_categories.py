# Generated by Django 4.1.6 on 2023-02-28 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0023_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(to='product.category'),
        ),
    ]
