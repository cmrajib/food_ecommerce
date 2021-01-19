from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

# Register your models here.
from shop.models import Product, Category



class CategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('category_name',), }


class ProductAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(object.image.url))

    thumbnail.short_description = 'Photo'

    list_display = ('id', 'thumbnail', 'title', 'stock','price','discountprice', 'Weight','DateArrived')
    list_display_links = ('id','thumbnail', 'title')
    list_filter = ['title']
    # list_editable = ('is_published',)
    search_fields =('user', 'title')
    list_per_page = 10

    prepopulated_fields = {'slug': ('title',), }


admin.site.register(Product,ProductAdmin)
admin.site.register(Category, CategoryAdmin)
