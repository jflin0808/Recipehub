# Generated by Django 3.2.5 on 2022-01-05 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20220105_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cookTime',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prepTime',
            field=models.TimeField(),
        ),
    ]