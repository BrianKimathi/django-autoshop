# add urls here

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('submit_comment/', views.submit_comment, name='submit_comment'),
    path('search/', views.search, name='search'),
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
]