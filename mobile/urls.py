from django.views.decorators.cache import cache_page
from django.urls import path
from .views import *

urlpatterns = [
    # path(r'^$', cart_detail, name='cart_detail'),
    path('cart_detail/', cart_detail, name='cart_detail'),
    path('add/<product_id>/', cart_add, name='cart_add'),
    # path(r'^add/(?P<product_id>\d+)/$', cart_add, name='cart_add'),
    path('remove/<int:product_id>/', cart_remove, name='cart_remove'),
    # path(r'^remove/(?P<product_id>\d+)/$', cart_remove, name='cart_remove'),
    path('create/', order_create, name='order_create'),
    path('', product_list, name='product_list'),
    path('brand/<brand_slug>', product_list, name='product_list_by_brand'),
    path('category/<category_slug>/', product_list, name='product_list_by_category'),
    path('<slug>/<int:id>', product_detail, name='product_detail'),
    # path('brand/<brand_slug>/', brands_list, name='brands_list')
    # path('test/', test, name='product_list'),
    ]
