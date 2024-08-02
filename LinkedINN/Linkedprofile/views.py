import requests
from django.shortcuts import render, redirect
from .models import *


def loading(request):
    return redirect(home)

def home(request):
    response = requests.get('https://fakestoreapi.com/products')
    if response.status_code == 200:
        products = response.json()
    else:
        products = []
    a=logo.objects.all()
    b=mains.objects.all()
    return render(request, 'index.html', {'products': products,'a1':a,'b1':b})

def mens(request):
    response = requests.get('https://fakestoreapi.com/products')
    if response.status_code == 200:
        products = response.json()
    else:
        products = []
    a=logo.objects.all()
    return render(request, 'mens.html', {'products': products,'a1':a})

def women(request):
    response = requests.get('https://fakestoreapi.com/products')
    if response.status_code == 200:
        products = response.json()
    else:
        products = []
    a=logo.objects.all()
    return render(request, 'women.html', {'products': products,'a1':a})

def jewelery(request):
    response = requests.get('https://fakestoreapi.com/products')
    if response.status_code == 200:
        products = response.json()
    else:
        products = []
    a=logo.objects.all()
    return render(request, 'jewelery.html', {'products': products,'a1':a})

def electronics(request):
    response = requests.get('https://fakestoreapi.com/products')
    if response.status_code == 200:
        products = response.json()
    else:
        products = []
    a=logo.objects.all()
    return render(request, 'electronics.html', {'products': products,'a1':a})

# def productdetails(request,ids):
#     id=int(ids)
#     response = requests.get('https://fakestoreapi.com/products')
#     if response.status_code == 200:
#         products = response.json()
#     else:
#         products = []
#     a=logo.objects.all()
#     return render(request, 'productview.html', {'products': products,'a1':a,'id':id})

def productdetails(request, ids):
    id = int(ids)  # Convert ids to integer
    response = requests.get('https://fakestoreapi.com/products')
    if response.status_code == 200:
        products = response.json()
        product = next((item for item in products if item['id'] == id), None)
    else:
        product = None
    
    a = logo.objects.all()
    return render(request, 'productview.html', {'product': product, 'a1': a, 'id': id})