from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings



urlpatterns = [
    # Define your URL patterns here
    path('products/', views.product_list, name='product-list'),
    path('products/<int:pk>/', views.product_commanded, name='product-commanded'),
    path('contact/', views.contact_message, name='contact-message'),
    path('order/', views.order, name='order')
]
