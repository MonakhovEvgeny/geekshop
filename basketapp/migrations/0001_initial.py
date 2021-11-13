# Generated by Django 2.2.24 on 2021-11-10 19:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [("mainapp", "0004_fill_db"), migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="Basket",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("quantity", models.PositiveIntegerField(default=0, verbose_name="количество")),
                ("add_datetime", models.DateTimeField(auto_now_add=True, verbose_name="время добавления")),
                ("product", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="mainapp.Product")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="basket", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        )
    ]
