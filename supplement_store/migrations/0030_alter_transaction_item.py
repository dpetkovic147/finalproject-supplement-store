# Generated by Django 4.2.3 on 2024-02-22 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplement_store', '0029_remove_transaction_total_price_alter_item_is_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplement_store.cart'),
        ),
    ]
