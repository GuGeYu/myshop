from django.urls import path
from .views import *

urlpatterns = [
    path('', product_list, name='product_list'),
    path('brand/<brand_slug>', product_list, name='product_list_by_brand'),
    path('category/<category_slug>/', product_list, name='product_list_by_category'),
    path('<slug>/<int:id>', product_detail, name='product_detail'),
    ]
