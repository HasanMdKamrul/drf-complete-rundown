# Generated by Django 4.0.8 on 2023-02-13 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_remove_product_category_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Like New', 'Like New'), ('Battery Health', 'Battery Health'), ('Featured', 'Featured')], default='Like New', max_length=255),
        ),
    ]