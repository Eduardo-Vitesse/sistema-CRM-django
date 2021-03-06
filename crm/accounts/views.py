from django.shortcuts import render, redirect
#from django.http import HttpResponse
from . models import *
from . forms import OrderForm

# Create your views here.

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    panding = orders.filter(status='Panding').count()

    context = {'orders': orders, 'customers': customers,
    'total_orders':total_orders,'delivered':delivered,
    'panding':panding}

    return render(request, 'dashboard.html', context)

def products(request):
    products = Products.objects.all()
    return render(request, 'products.html', {'products':products})

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()

    context = {'customer':customer, 'orders':orders, 'order_count':order_count}

    return render(request, 'customer.html', context)

def createOrder(request):

    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'order_form.html', context)

def updateOrder(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'order_form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item':order}
    return render(request, 'delete.html', context)
