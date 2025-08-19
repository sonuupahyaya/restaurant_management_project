from django.contrib import admin
from .models import Menu, Order

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price")  # show these columns in admin list
        search_fields = ("name",)               # allow searching by name
            list_filter = ("price",)                # allow filtering by price


            @admin.register(Order)
            class OrderAdmin(admin.ModelAdmin):
                list_display = ("id", "customer_name", "status", "total_amount", "created_at")
                    search_fields = ("customer_name", "status")
                        list_filter = ("status", "created_at")
                        