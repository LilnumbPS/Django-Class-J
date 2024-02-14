# Generated by Django 5.0 on 2024-02-06 03:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_alter_product_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100, verbose_name='رنگ')),
                ('size', models.CharField(max_length=100, verbose_name='اندازه')),
            ],
            options={
                'verbose_name': 'اطلاعات تکمیلی',
                'verbose_name_plural': 'لیست اطلاعات تکمیلی',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='product_info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blogs.productinformation', verbose_name='اطلاعات تکمیلی'),
        ),
    ]
