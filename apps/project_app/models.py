# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..login_app.models import User
from datetime import datetime
import re
date_regex = re.compile(r'^(\d+-\d+-\d+)+$')


class UserManager(models.Manager):
    def add_item(self, item_data, session):
        flag = True
        errors = []


        if len(item_data['item']) < 1:
            flag = False
            errors.append('Please enter an item.')

        if len(item_data['item']) < 3:
            flag = False
            errors.append('Please enter an item using 3+ characters.')



        if flag:
            new_item = Item.objects.create(item=item_data['item'], created_by= session)
            return True
        else:
            return (False, errors)

class Item(models.Model):
    item = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=255, default = True)

    objects = UserManager()
    def __str__(self):
        return self.name

class User_Item(models.Model):
    user_item = models.ForeignKey(Item, related_name='useritem')
    user = models.ForeignKey(User, related_name='itemuser')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
