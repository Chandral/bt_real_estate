# Generated by Django 2.2.3 on 2019-07-24 08:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0004_auto_20190722_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 7, 24, 13, 39, 53, 626557)),
        ),
    ]
