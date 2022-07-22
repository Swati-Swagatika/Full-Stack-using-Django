from django.contrib import admin

from .models import Cuisine,Food


class CuisineAdmin(admin.ModelAdmin):
    list_display= ('category', 'created_at')
    ordering = ('category',)
class FoodAdmin(admin.ModelAdmin):
    list_display= ('name', 'price','is_available')
    ordering = ('name',)
    list_editable= ('is_available',)
    search_fields = ('name',)
    list_filter = ('is_available',)

# admin.site.register(Cuisine)
admin.site.register(Cuisine, CuisineAdmin)
admin.site.register(Food, FoodAdmin)
