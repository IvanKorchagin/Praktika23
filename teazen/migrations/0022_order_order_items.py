# Generated by Django 4.1.7 on 2023-04-04 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teazen', '0021_remove_order_items_remove_orderitem_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_items',
            field=models.ManyToManyField(to='teazen.orderitem'),
        ),
    ]
