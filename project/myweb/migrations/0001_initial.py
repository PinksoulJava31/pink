# Generated by Django 4.1.1 on 2023-01-31 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=25)),
                ('product_price', models.IntegerField()),
                ('product_quantity', models.IntegerField()),
            ],
        ),
    ]
