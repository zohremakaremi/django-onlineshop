# Generated by Django 4.1.2 on 2022-10-31 13:29

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetting',
            name='about_us',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
