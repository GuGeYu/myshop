from django import template
from ..models import Category, Brand
from django.db.models import Count, F
from django.core.cache import cache

register = template.Library()


# @register.simple_tag(name='get_list_categories')
# def get_categories():
#     return Category.objects.all()

@register.inclusion_tag('mobile/list_for_side.html')
def show_side_bar():
    # categories = Category.objects.all()
    # categories = cache.get('categories')
    # if not categories:
    #     categories = Category.objects.annotate(cnt=Count('news', filter=F("news__is_published"))).filter(cnt__gt=0)
    #     cache.set('categories',categories, 30 )
    # categories = Category.objects.annotate(cnt=Count('product', filter=F("product__available"))).filter(cnt__gt=0)
    # brands = Brand.objects.annotate(cnt=Count('product', filter=F("product__available"))).filter(cnt__gt=0)
    categories = Category.objects.all()
    brands = Brand.objects.all()

    return {'categories': categories, 'brands': brands}
