from django.shortcuts import render
from .models import Product, Category, Cart, OrderItem, Brand
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .forms import CartAddProductForm, OrderCreateForm
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


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'mobile/cart_detail.html', {'cart': cart})


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return render(request, 'mobile/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'mobile/create.html', {'cart': cart, 'form': form})
