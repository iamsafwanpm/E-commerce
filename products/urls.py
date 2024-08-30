from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('',views.index ,name='home'),
    path ('products_list/',views.list_products,name='list_products'),
    path ('product_details/<pk>',views.detail_product,name='detail_product'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)