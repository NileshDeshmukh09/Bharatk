from django.contrib import admin
# Register your models here.
# Create your models here.
from .models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):

    list_display = ('user' , 'mobile_num')






# admin.site.register(ExtendedUser)
admin.site.register(Contact,ContactAdmin)