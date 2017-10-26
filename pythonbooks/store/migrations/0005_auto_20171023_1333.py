# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-23 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_price_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='cover',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='book',
            name='offer_url',
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]