# Generated by Django 4.2.11 on 2024-04-27 10:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contribute", "0007_alter_item_item_deposit_require"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="item_deposit_require",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
    ]
