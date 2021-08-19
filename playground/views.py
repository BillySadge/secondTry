from django.db.models.expressions import Col
from django.db.models.fields import DecimalField
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist 
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q, F, Value, Func, ExpressionWrapper
from django.db.models.aggregates import Count, Max, Min, Avg
from django.db.models.functions import Concat
from django.db import transaction, connection
from store.models import Collection, Product, OrderItem, Order, Customer
from tags.models import Tag, TaggedItem

def say_hello(request):
    
    return render(request, 'hello.html', {'name': 'Andrey'}) 