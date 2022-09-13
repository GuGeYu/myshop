from django.contrib import admin
from .models import Category, Product, Brand

# from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


# class ProductAdminForm(forms.ModelForm):
#     content = forms.CharField(widget=CKEditorUploadingWidget()) # переопределяет это поле в заданной модели, название должно совпадать
#     class Meta:
#         model = Product # связан с этой моделью
#         fields = '__all__'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'brand', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    list_display_links = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)

admin.site.site_title = 'Админка'
admin.site.site_header = 'Админка'
