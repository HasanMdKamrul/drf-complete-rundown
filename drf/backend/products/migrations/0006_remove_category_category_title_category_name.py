# Generated by Django 4.0.8 on 2023-02-13 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_category_products_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_title',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Like New', 'Like New'), ('Battery Health', 'Battery Health'), ('Featured', 'Featured')], default='Like New', max_length=255),
        ),
    ]
