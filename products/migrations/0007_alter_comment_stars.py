# Generated by Django 4.2.1 on 2023-07-04 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_active_alter_product_datetime_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='stars',
            field=models.CharField(choices=[('*', 'Very Bad'), ('**', 'Bad'), ('***', 'Normal'), ('****', 'Good'), ('*****', 'Very Good')], max_length=10, verbose_name='What is your Score?'),
        ),
    ]
