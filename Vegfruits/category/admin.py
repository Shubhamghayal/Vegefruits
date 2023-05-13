from .models import Category
from django.contrib import admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("categoryname", 'cat_image')
    prepopulated_fields = {"slug": ('categoryname',)}


admin.site.register(Category, CategoryAdmin)

