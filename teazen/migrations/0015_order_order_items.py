# Generated by Django 4.1.7 on 2023-04-04 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teazen', '0014_remove_order_items_alter_order_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_items',
            field=models.ManyToManyField(to='teazen.orderitem'),
        ),
    ]
