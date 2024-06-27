# Generated by Django 5.0.6 on 2024-06-27 08:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('full_name', models.CharField(max_length=255)),
                ('mobile_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('weight', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='HeartInfo',
            fields=[
                ('Customer_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='prediction.registerdetail')),
                ('Age', models.IntegerField(blank=True, null=True)),
                ('Gender', models.CharField(blank=True, max_length=6, null=True)),
                ('Cp', models.IntegerField(blank=True, null=True)),
                ('Trestbps', models.IntegerField(blank=True, null=True)),
                ('Chol', models.IntegerField(blank=True, null=True)),
                ('Fbs', models.IntegerField(blank=True, null=True)),
                ('Restecg', models.IntegerField(blank=True, null=True)),
                ('Mhra', models.IntegerField(blank=True, null=True)),
                ('Exang', models.IntegerField(blank=True, null=True)),
                ('Oldpeak', models.FloatField(blank=True, null=True)),
                ('Slope', models.IntegerField(blank=True, null=True)),
                ('Ca', models.IntegerField(blank=True, null=True)),
                ('Thal', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
