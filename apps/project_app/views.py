# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Item, User_Item, User
from django.shortcuts import render, redirect
from django.contrib import messages
from sets import Set


def items(request):
    a = set(Item.objects.all())
    b= set(Item.objects.filter(useritem__user__username=request.session['username']))
    excluded_items = (a.difference(b))
    context = {
    'user_item' : User_Item.objects.filter(user__username = request.session['username']),
    'all_other_user_items': excluded_items,
    'all_users':User.objects.all()
    }

    return render (request,'project_app/index.html', context)
def add_item(request):
    return render (request,'project_app/add_item.html')

def process_item(request):
    session = request.session['username']
    process_result = Item.objects.add_item(request.POST, session)


    if process_result == True:


        i1 = Item.objects.filter(item = request.POST['item'])
        u1 = User.objects.filter(username = request.session['username'])

        item_join = User_Item.objects.create(user=u1[0], user_item=i1[0])
        return redirect ('/items')

    else:
        for i in process_result[1]:
            messages.info(request,i)
        return redirect ('/items/add')

def wish_items(request, item_id):
    context ={
    'item_filter':Item.objects.filter(id=item_id),
    'users_of_item':User_Item.objects.filter(user_item__id=item_id)
    }
    return render(request,'project_app/wish_items.html', context)

def join(request, item_id):
    i1 = Item.objects.filter(id = item_id)
    u1 = User.objects.filter(username = request.session['username'])

    item_join = User_Item.objects.create(user=u1[0], user_item=i1[0])
    return redirect ('/items')

def remove(request, item_id):
    User_Item.objects.filter(user_item__id=item_id).filter(user__username=request.session['username']).delete()
    return redirect ('/items')

def delete(request, item_id):
    Item.objects.filter(id=item_id).delete()
    return redirect ('/items')

# Create your views here.
