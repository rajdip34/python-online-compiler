# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-30 04:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('currency', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.BigAutoField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=50)),
                ('bloombergticker', models.CharField(db_column='BloombergTicker', max_length=50)),
                ('reutersric', models.CharField(db_column='ReutersRic', max_length=50)),
                ('bloombergid', models.CharField(db_column='BloombergID', max_length=50)),
                ('modifydatetime', models.DateTimeField(db_column='ModifyDateTime')),
                ('active', models.IntegerField(blank=True, db_column='Active', null=True)),
                ('customindex', models.IntegerField(blank=True, null=True)),
                ('customindexconfiguration', models.CharField(blank=True, max_length=20000, null=True)),
                ('currencyid', models.ForeignKey(db_column='CurrencyId', on_delete=django.db.models.deletion.DO_NOTHING, to='currency.Currency')),
                ('modifyuser', models.ForeignKey(blank=True, db_column='ModifyUserid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'index',
                'managed': True,
            },
        ),
    ]
