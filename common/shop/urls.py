from django.urls import path
from .views import save_order, ProductListView,  ProductDetailView, CategoryDetailView

urlpatterns = [
    path("", ProductListView.as_view(), name='product_list_url'),
    path("products/<int:pk>/", ProductDetailView.as_view(), name='product_detail_url'),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name='category_detail_url'),
    path("save_order", save_order)
]
