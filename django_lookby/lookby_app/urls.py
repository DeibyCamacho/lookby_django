from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('recuperar/', views.recover_view, name='recover'),
    path('reset-password/', views.reset_password_view, name='reset_password'),
    path('logout/', views.logout_view, name='logout'),
    path('cliente/', views.client_dashboard, name='client_dashboard'),
    path('negocio/', views.business_dashboard, name='business_dashboard'),
    path('proveedor/', views.supplier_dashboard, name='supplier_dashboard'),
    path('superadmin/', views.superadmin_dashboard, name='superadmin_dashboard'),
]
