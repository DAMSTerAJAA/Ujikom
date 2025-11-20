from django.contrib import admin
from .models import *
# Register your models here.

admin.site.index_title = "AndiGunshop"
admin.site.site_header = "Andi Gunshop"
admin.site.site_title = "Andi Gunshop"
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("name",)}

admin.site.register(Product, ProductAdmin)
