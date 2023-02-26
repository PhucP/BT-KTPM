# Generated by Django 4.1.7 on 2023-02-25 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField()),
                ('status', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'cart',
            },
        ),
    ]
