from django.conf.urls import url, include
from django.views.generic import RedirectView

from mysite.products import views


urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='products_list'), name='home'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'products/$', views.products_list, name='products_list'),
    url(r'products/categories/new/$', views.new_category, name='new_category'),
    url(r'products/new/$', views.new_product, name='new_product'),
    url(r'products/edit_all/$', views.edit_all_products, name='edit_all_products'),
]
