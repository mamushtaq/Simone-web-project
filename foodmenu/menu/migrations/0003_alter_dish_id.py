# Generated by Django 3.2.4 on 2021-07-01 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_dish_added_to_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
