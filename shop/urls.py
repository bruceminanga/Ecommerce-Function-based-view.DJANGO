from django.urls import path
from . import views
from . views import ListView, DetailView
app_name = 'shop'
urlpatterns = [
    path('', ListView.as_view(), name='product_list'),
    path('<slug:category_slug>/', ListView.as_view(),
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', DetailView.as_view(),
         name='product_detail'),
]
