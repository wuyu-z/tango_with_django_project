from dataclasses import field
from django.contrib import admin
from rango.models import Category,Page
from rango.models import UserProfile

class PageAdmin(admin.ModelAdmin):
    list_display=('title','category','url')
    prepolulated_field={'slug':('name',)}

admin.site.register(Category)
admin.site.register(Page,PageAdmin)
admin.site.register(UserProfile)
# Register your models here.
