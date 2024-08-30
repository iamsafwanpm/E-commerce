from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    featured_products=Product.objects.order_by('priority')[:4]
    latest_product=Product.objects.order_by('-id')[:4]
    context={'featured_products':featured_products,
             'latest_products':latest_product
             }
    return render (request,'index.html',context)

def list_products(request):
    """
    Return a list of products, with optional search functionality and pagination.
    """
    
    query = request.GET.get('q', '')  
    page = request.GET.get('page', 1)

    if query:
        products_list = Product.objects.filter(title__icontains=query).order_by('priority')
    else:
        products_list = Product.objects.order_by('priority')

    product_paginator = Paginator(products_list, 16)
    products_list = product_paginator.get_page(page)
    
    context = {
        'products': products_list,
        'query': query
    }
    
    return render(request, 'products.html', context)


def detail_product(request,pk):
    product=Product.objects.get(pk=pk)
    context={'product':product}
    return render (request,'product_details.html',context)
