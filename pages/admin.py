from django.contrib import admin
from pages.models import *

# Register your models here.

@admin.register(MainScrollModel)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['title', 'discount', 'created_at', 'updated_at']
    search_fields = ['title', 'info']
    list_filter = ['created_at', 'updated_at']
    
    
# @admin.register(Menu)
# class ModelNameAdmin(admin.ModelAdmin):
#     list_display = ['title', 'price', 'created_at', 'updated_at']
#     search_fields = ['title', 'info']
#     list_filter = ['created_at', 'updated_at']

admin.site.register(Menu)
