# Generated by Django 4.1.2 on 2022-10-25 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_sub', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('link', models.URLField(max_length=100)),
                ('sub_menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='smenu', to='eshop_menu.menu')),
            ],
            options={
                'verbose_name': 'منو',
                'verbose_name_plural': 'منوها',
                'ordering': ('name',),
            },
        ),
    ]
