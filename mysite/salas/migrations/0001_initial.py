# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-01 05:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=4000)),
                ('discount', models.FloatField()),
                ('available', models.BooleanField()),
                ('deleted', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=4000)),
                ('price', models.FloatField()),
                ('picture_format', models.CharField(max_length=50)),
                ('available', models.BooleanField()),
                ('uploaded', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_gross', models.FloatField()),
                ('total_net', models.FloatField()),
                ('sale_date', models.DateTimeField()),
                ('details', models.TextField()),
                ('deleted', models.BooleanField()),
                ('comments', models.CharField(max_length=4000)),
                ('completed', models.BooleanField()),
                ('personal_id', models.PositiveIntegerField()),
                ('coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salas.Coupon')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('deleted', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('email_public', models.BooleanField()),
                ('given_name', models.CharField(max_length=50)),
                ('given_name_visible', models.BooleanField()),
                ('family_name', models.CharField(max_length=50)),
                ('family_name_visible', models.BooleanField()),
                ('phone_number', models.CharField(max_length=50)),
                ('phone_number_public', models.BooleanField()),
                ('language', models.CharField(max_length=50)),
                ('is_dist', models.BooleanField()),
                ('payment_instructions', models.CharField(max_length=50)),
                ('new_period', models.DurationField()),
                ('sale_id_prefix', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salas.User')),
            ],
        ),
        migrations.AddField(
            model_name='tag',
            name='distributor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salas.User'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='salas.User'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='distributor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='salas.User'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='products',
            field=models.ManyToManyField(to='salas.Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='distributor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salas.User'),
        ),
        migrations.AddField(
            model_name='coupon',
            name='distributor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salas.User'),
        ),
    ]