from django.contrib import admin

from django.contrib import admin
from .models import Category, Book
 
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)
 
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'category', 'author', 'item_id']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Book, BookAdmin)


