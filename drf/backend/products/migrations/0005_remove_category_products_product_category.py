# Generated by Django 4.0.8 on 2023-02-13 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='products',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category'),
        ),
    ]
