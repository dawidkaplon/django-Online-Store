# Generated by Django 4.2.3 on 2023-08-09 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='photo',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
