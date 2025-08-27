from django.contrib import admin
from .models import Menu, Order
from .models import
from .models import Contact
from.models import RestaurantLocation
from .models import MenuItem

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    
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
OrderItem                        


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price")
        search_fields = ("name",)


        class OrderItemInline(admin.TabularInline):
            model = OrderItem
                extra = 1


                @admin.register(Order)
                class OrderAdmin(admin.ModelAdmin):
                    list_display = ("id", "customer", "status", "total_amount", "created_at")
                        search_fields = ("customer__username", "status")
                            list_filter = ("status", "created_at")
                                inlines = [OrderItemInline]


                                @admin.register(OrderItem)
                                class OrderItemAdmin(admin.ModelAdmin):
                                    list_display = ("id", "order", "menu_item", "quantity")
 from .models import UserProfile                                   

 admin.site.register(UserProfile)
 
 @admin.register(Menu)
 class MenuAdmin(admin.ModelAdmin):
     list_display = ("name", "price")
         search_fields = ("name", "description")
RestaurantLocation

admin.site.register(RestaurantLocation)
admin.site.register(Contact)
admin.site.register(RestaurantLocation)
