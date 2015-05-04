# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='user',
            field=models.ForeignKey(related_name='transfers', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='account',
            field=models.ForeignKey(related_name='transactions', to='accounts.Account'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transfer',
            field=models.ForeignKey(related_name='transactions', to='accounts.Transfer'),
        ),
        migrations.AddField(
            model_name='accountsecondaryusers',
            name='account',
            field=models.ForeignKey(to='accounts.Account'),
        ),
        migrations.AddField(
            model_name='accountsecondaryusers',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='account',
            name='account_type',
            field=models.ForeignKey(related_name='accounts', to='accounts.AccountType', null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='primary_user',
            field=models.ForeignKey(related_name='accounts', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='secondary_users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='accounts.AccountSecondaryUsers', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='transaction',
            unique_together=set([('transfer', 'account')]),
        ),
    ]
