# Generated by Django 4.0.3 on 2022-03-23 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_brand_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_image',
            name='link',
            field=models.CharField(default='/product/zara-pink-shirt', max_length=150),
            preserve_default=False,
        ),
    ]
