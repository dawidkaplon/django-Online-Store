# Generated by Django 4.2.3 on 2023-08-17 17:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0005_cartitem_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="price",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
