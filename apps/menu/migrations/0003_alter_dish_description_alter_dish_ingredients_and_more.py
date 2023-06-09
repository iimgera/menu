# Generated by Django 4.2 on 2023-04-29 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_menu_options_remove_ingredient_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='ingredients',
            field=models.ManyToManyField(blank=True, to='menu.ingredient', verbose_name='Ингредиенты'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена'),
        ),
    ]
