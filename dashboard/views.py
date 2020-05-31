from django.shortcuts import render

# Create your views here.

def dashboard(request):
    context = {}
    return render(request, 'dashboard.html', context)

def product(request):
    context = {}
    return render(request, 'product/product.html', context)

def customer(request):
    context = {}
    return render(request, 'customer/customer.html', context)

def order(request):
    context = {}
    return render(request, 'order/order.html', context)       


def ship(request):
    context = {}
    return render(request, 'ship/ship.html', context)

def vendor(request):
    context = {}
    return render(request, 'vendor/vendor.html', context)    