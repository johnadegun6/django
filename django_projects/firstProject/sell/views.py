from django.shortcuts import render
from django.http import HttpResponse
from.models import Store, Products, Category
from django.template import Template

# Create your views here.

def show_home_page(request):
    return HttpResponse('<h1> Hi, Patronise my boutique!<h1>')


# def web_page(products):
#     page = '<ul>'
#     for product in products:
#         page += f"""<li><h1>{product['name']}</h1><h2>{product['desc']}</h2><p>{product['price']}, </p></li>"""
#     page += '</ul>'
#     return page


# def store_page(stores):
#     page = '<ul>'
#     for store in stores:
#         page += f"""<li><h1>{store.name}</h1><h2>{store.tagline}</h2><p>{store.owner.first_name}, welcome </p></li>"""
#     page += '</ul>'
#     return page


def products(request):
    products = Products.objects.all() #.values()
    categories = Category.objects.all()
    
    #webpage = web_page(products)
    context = {'products' : products, 'categories' : categories}
    return render(request, 'sell/products.html', context) #HttpResponse(webpage)

def product(request, id):
    product = Products.objects.filter(id=id).values()

    # webPage = web_page(product)
    # return HttpResponse(webPage)

def stores(request):
    stores = Store.objects.all() #.values()
    # return HttpResponse(web_page(stores))
    

def categories(request):
    categories = Category.objects.all().values()
    webpage = web_page(categories)
    return HttpResponse(webpage)

def category(request, id):
    category = Category.objects.filter(id=id).values()
    webpage = web_page(category)
    return HttpResponse(webpage)

def store(request, id):
    pass

def store_products(request, id):
    pass

