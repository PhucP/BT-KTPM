# Generated by Django 4.1.6 on 2023-02-28 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0030_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='This field is for product description'),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(default='D:/School stuffs/P1/images/capacitor.jpg', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(to='product.category'),
        ),
    ]
