from django.urls import path
from clinet import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.dashboard_login, name="login"),
    path('logout/', views.dashboard_logout, name="logout"),
    path('category_list/', views.category_list, name="category_list"),
    path('category_create/', views.category_create, name="category_create"),
    path('<int:pk>category_edit/', views.category_edit, name="category_edit"),
    path('<int:pk>/category_delete/', views.category_delete, name="category_delete"),
    path('product_list/', views.product_list, name="product_list"),
    path('product_create/', views.product_create, name="product_create"),
    path('<int:pk>product_edit/', views.product_edit, name="product_edit"),
    path('<int:pk>/product_delete/', views.product_delete, name="product_delete"),
    path('kontak_create/', views.kontak_create, name="kontak_create"),
    path('kontak_list/', views.kontak_list, name='kontak_list' ),
    path('<int:pk>/kontak_edit/', views.kontak_edit, name="kontak_edit"),
    path('<int:pk>/kontak_delete/', views.kontak_delete, name="kontak_delete"),


]