from django.shortcuts import render

# Create your views here.

def finance(request):
    context = {}
    return render(request, 'finance.html', context)

def expense(request):
    context = {}
    return render(request, 'expense/expense.html', context)


def revenue(request):
    context = {}
    return render(request, 'revenue/revenue.html', context)


def sales(request):
    context = {}
    return render(request, 'sales/sales.html', context)
