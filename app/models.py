# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import requests
import json 

from decimal import Decimal
import datetime

from safedelete import safedelete_mixin_factory, SOFT_DELETE, \
    DELETED_VISIBLE_BY_PK, safedelete_manager_factory, DELETED_INVISIBLE

class TimeStampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


SoftDeleteMixin = safedelete_mixin_factory(policy=SOFT_DELETE,
                                           visibility=DELETED_VISIBLE_BY_PK)


class SoftDeletableModel(SoftDeleteMixin):
    disabled = models.BooleanField(default=False)
    active_objects = safedelete_manager_factory(models.Manager, 
                                                models.QuerySet,
                                                DELETED_INVISIBLE)()

    class Meta:
        abstract = True


class Currency(TimeStampedModel, SoftDeletableModel):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    k_code = models.CharField(max_length=10)  # Kraken code 

    def __str__(self):
        return self.name
