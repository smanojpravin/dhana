from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path


import store.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/<int:id>/', store.views.show, name='show-product'),
    path('cart/', store.views.cart, name='shopping-cart'),
    path('', store.views.index, name='list-products'),
    path('home', store.views.home, name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
