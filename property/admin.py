from django.contrib import admin

# Register your models here.
from .models import Category, PropertyImages, Property, Order

import admin_thumbnails
# Register your models here.

@admin_thumbnails.thumbnail('product_img')
class PropertyImagesInline(admin.TabularInline):
    model = PropertyImages
    extra = 1

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'category' , 'price','img' )
    inlines = [PropertyImagesInline]


admin.site.register(Category),
admin.site.register(Property,PropertyAdmin),
admin.site.register(PropertyImages),
admin.site.register(Order),
