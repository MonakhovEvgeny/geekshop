# Generated by Django 2.2.24 on 2021-12-15 14:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [("authnapp", "0007_auto_20211211_1424")]

    operations = [
        migrations.AlterField(
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2021, 12, 17, 14, 12, 9, 307675, tzinfo=utc),
                verbose_name="актуальность ключа",
            ),
        )
    ]
