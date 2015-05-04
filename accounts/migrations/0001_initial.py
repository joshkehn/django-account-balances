# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, unique=True, null=True, blank=True)),
                ('description', models.TextField(help_text='This text is shown to customers during checkout', null=True, blank=True)),
                ('code', models.CharField(max_length=128, unique=True, null=True, blank=True)),
                ('status', models.CharField(default=b'Open', max_length=32)),
                ('credit_limit', models.DecimalField(default=Decimal('0.00'), null=True, max_digits=12, decimal_places=2, blank=True)),
                ('balance', models.DecimalField(default=Decimal('0.00'), null=True, max_digits=12, decimal_places=2)),
                ('start_date', models.DateTimeField(null=True, blank=True)),
                ('end_date', models.DateTimeField(null=True, blank=True)),
                ('can_be_used_for_non_products', models.BooleanField(default=True, help_text=b'Whether this account can be used to pay for shipping and other charges')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AccountSecondaryUsers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(unique=True, max_length=255)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('code', models.CharField(max_length=128, unique=True, null=True, blank=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IPAddressRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip_address', models.IPAddressField(unique=True, verbose_name='IP address')),
                ('total_failures', models.PositiveIntegerField(default=0)),
                ('consecutive_failures', models.PositiveIntegerField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_last_failure', models.DateTimeField(null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'IP address record',
                'verbose_name_plural': 'IP address records',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=12, decimal_places=2)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reference', models.CharField(max_length=64, unique=True, null=True)),
                ('amount', models.DecimalField(max_digits=12, decimal_places=2)),
                ('merchant_reference', models.CharField(max_length=128, null=True)),
                ('description', models.CharField(max_length=256, null=True)),
                ('username', models.CharField(max_length=128)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('destination', models.ForeignKey(related_name='destination_transfers', to='accounts.Account')),
                ('parent', models.ForeignKey(related_name='related_transfers', to='accounts.Transfer', null=True)),
                ('source', models.ForeignKey(related_name='source_transfers', to='accounts.Account')),
            ],
            options={
                'ordering': ('-date_created',),
                'abstract': False,
            },
        ),
    ]
