# Generated by Django 4.1.2 on 2022-10-31 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='visit_count',
            field=models.IntegerField(default=0),
        ),
    ]
