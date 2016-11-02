# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-01 23:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='available',
            new_name='enabled',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='available',
            new_name='enabled',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_dist',
        ),
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('C', 'Customer'), ('D', 'Distributor')], default='Distributor', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='uploaded',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='distributor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='salas.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='new_period',
            field=models.DurationField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='payment_instructions',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='sale_id_prefix',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]