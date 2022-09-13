from django.shortcuts import render
from .models import Product, Category, Brand
from django.shortcuts import get_object_or_404
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator


def test(request):
    products = Product.objects.all()
    return render(request, 'mobile/test.html', {'products': products})


def product_list(request, category_slug=None, brand_slug=None):
    category = None
    brand = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    brands = Brand.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        paginator = Paginator(products, 6)  # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request,
                      'mobile/list.html',
                      {'category': category,
                       'categories': categories,
                       # 'products': products,
                       'brands': brands,
                       'page_obj': page_obj})
    elif brand_slug:
        brand = get_object_or_404(Brand, slug=brand_slug)
        products = products.filter(brand=brand)
        paginator = Paginator(products, 6)  # Show 25 contacts per page.
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)
        return render(request,
                      'mobile/list.html',
                      {'brand': brand,
                       'categories': categories,
                       # 'products': products,
                       'brands': brands,
                       'page_obj': page_obj})
    else:
        paginator = Paginator(products, 6)  # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request,
                      'mobile/list.html',
                      {'categories': categories,
                       # 'products': products,
                       'brands': brands,
                       'page_obj': page_obj})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'mobile/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})
