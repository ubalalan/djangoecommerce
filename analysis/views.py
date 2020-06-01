from django.shortcuts import render

# Create your views here.

def analysis(request):
    context = {}
    return render(request, 'analysis.html', context)

def competitor(request):
    context = {}
    return render(request, 'competitor/competitor.html', context)

def financial(request):
    context = {}
    return render(request, 'financial/financial.html', context)       


def market(request):
    context = {}
    return render(request, 'market/market.html', context)
 
def products(request):
    context = {}
    return render(request, 'products/products.html', context)   


