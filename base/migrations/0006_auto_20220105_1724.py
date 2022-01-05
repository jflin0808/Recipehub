# Generated by Django 3.2.5 on 2022-01-05 22:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0005_diet_meal_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='diet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.diet'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='meal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.meal'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='servings',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
