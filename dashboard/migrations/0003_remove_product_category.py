# Generated by Django 3.0.6 on 2020-06-02 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
