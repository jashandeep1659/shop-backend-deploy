# Generated by Django 4.0.3 on 2022-03-20 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paid_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='paid_char',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]