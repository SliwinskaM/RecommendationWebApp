# Generated by Django 3.2.9 on 2021-12-03 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='idx',
            field=models.IntegerField(default='-1'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='nic', max_length=120),
        ),
        migrations.AlterField(
            model_name='product',
            name='shop_name',
            field=models.CharField(default='żodyn', max_length=120),
        ),
    ]
