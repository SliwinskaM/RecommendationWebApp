# Generated by Django 3.2.9 on 2021-12-02 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idx', models.IntegerField()),
                ('name', models.CharField(max_length=120)),
                ('shop_name', models.CharField(max_length=120)),
            ],
        ),
    ]
