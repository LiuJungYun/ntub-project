# Generated by Django 4.2.10 on 2024-02-20 11:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('borrow', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='returndate',
            new_name='end_time',
        ),
        migrations.AddField(
            model_name='order',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
