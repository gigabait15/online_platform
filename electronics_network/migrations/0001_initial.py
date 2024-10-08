# Generated by Django 5.1 on 2024-08-17 13:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=255)),
                ('house_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('release_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ENetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('debt', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('level_network', models.PositiveIntegerField(choices=[(0, 'Factory'), (1, 'Retail Network'), (2, 'Sole Trader')], default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('contact', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='electronics_network.contact')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supplied', to='electronics_network.enetwork')),
                ('products', models.ManyToManyField(blank=True, to='electronics_network.product')),
            ],
        ),
    ]
