# Generated by Django 4.0.2 on 2024-04-12 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('meal_types', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('meal_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='meal_types.mealtype')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
