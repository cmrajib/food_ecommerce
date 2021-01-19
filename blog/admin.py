from .models import Category, Post, Comment, Newsletter
from django.contrib import admin
# from django_summernote.admin import SummernoteModelAdmin


class CategoryAdmin( admin.ModelAdmin):
    prepopulated_fields = {"slug": ("category_name",)}

class PostAdmin( admin.ModelAdmin):  # instead of ModelAdmin
    # summernote_fields = '__all__'
    list_display = ['title' ,'author', 'category', 'created']
    search_fields = ['title', 'content' ]
    list_filter = ('category','tags')

    prepopulated_fields = {"slug": ("title",)}



admin.site.register(Post , PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)
admin.site.register(Newsletter)