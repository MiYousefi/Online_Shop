# Generated by Django 4.2.1 on 2023-06-17 19:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_image_alter_comment_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='datetime_created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Time of Creation'),
        ),
    ]
