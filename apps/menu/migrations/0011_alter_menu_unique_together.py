# Generated by Django 4.2 on 2023-04-30 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_remove_dish_category'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='menu',
            unique_together=set(),
        ),
    ]