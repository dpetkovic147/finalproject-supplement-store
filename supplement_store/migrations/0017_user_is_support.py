# Generated by Django 4.2.3 on 2023-09-30 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplement_store', '0016_supportanswer_date_alter_support_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_support',
            field=models.BooleanField(default=False),
        ),
    ]