# Generated by Django 3.2.9 on 2021-12-09 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='nic', max_length=120)),
                ('products', models.CharField(max_length=500)),
                ('shop', models.CharField(max_length=120)),
            ],
        ),
    ]
