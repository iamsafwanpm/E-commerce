from django.contrib import admin
from orders .models import Order
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_filter =[
        "owner",
        "order_status",
        "cretated_at",
    ]
    search_fields = (
        "owner",
        "id",
    )

admin.site.register(Order,OrderAdmin)
