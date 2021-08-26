from products.models import Product
from django.contrib import admin

# Register your models here.

admin.site.register(Product)

class ArticleAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
