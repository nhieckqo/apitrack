# Generated by Django 3.1.2 on 2021-01-19 02:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentstatus',
            name='entry_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 19, 10, 2, 39, 414337)),
        ),
    ]