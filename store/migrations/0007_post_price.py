# Generated by Django 4.2.2 on 2023-06-23 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_remove_post_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.DecimalField(decimal_places=2, default=5, max_digits=10),
        ),
    ]
