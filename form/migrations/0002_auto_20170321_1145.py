# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 11:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='email',
            new_name='epost',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='happy',
            new_name='glad',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='product',
            new_name='linje',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='customer_name',
            new_name='navn',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='details',
            new_name='tilbakemelding',
        ),
    ]
