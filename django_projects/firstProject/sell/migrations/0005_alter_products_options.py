# Generated by Django 4.2.1 on 2023-05-17 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0004_products_store'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('name', '-price'), 'verbose_name': 'Products'},
        ),
    ]
