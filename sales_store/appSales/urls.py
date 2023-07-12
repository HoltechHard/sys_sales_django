from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('category_list', views.category_list, name = 'category_list'),
    path('brand_list', views.brand_list, name = 'brand_list'), 
    path('product_list', views.product_list, name = 'product_list'),
    path('category_product_list/<int:cat_id>', views.category_product_list, name = 'category_product_list'),
    path('brand_product_list/<int:brand_id>', views.brand_product_list, name = 'brand_product_list'),
    path('product/<str:slug>/<int:id>', views.product_detail, name = 'product_detail'),
]