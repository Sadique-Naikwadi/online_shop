# Generated by Django 4.2 on 2024-05-29 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_image'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OderItems',
            new_name='OrderItems',
        ),
        migrations.AlterModelOptions(
            name='orderitems',
            options={'verbose_name_plural': 'OrderItems'},
        ),
    ]