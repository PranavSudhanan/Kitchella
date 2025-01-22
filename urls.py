from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    # Home and Account URLs
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.new_user, name='new_user'),
    path('accounts/register_company/', views.new_company, name='new_company'),
    path('accounts/register_employee/', views.new_employee, name='new_employee'),
    path('accounts/register_manager/', views.new_manager, name='new_manager'),
    path('accounts/details/', views.update_profile, name='update_profile'),
    path('accounts/delete/', views.delete_profile, name='delete_profile'),
    path ('accounts/change_password', views.change_password, name='change_password'),

    # Product and Category URLs
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_page, name='product_page'),
    path('categories/', views.categories, name='categories'),
    path('categories/<int:category_id>/', views.category_products, name='category_products'),
    path('new_product/', views.new_product, name='new_product'),
    
    # Search urls
    path('search/', views.search, name='search'),
    
    # Cart and Checkout URLs
    path('cart/', views.cart, name='cart'),
    path('cart/empty/', views.empty_cart, name='empty_cart'),
    path('cart/delete/<int:cart_item_id>/', views.delete_cart, name='delete_cart'),
    path('checkout/', views.checkout, name='checkout'),

    # Payment and Shipping URLs
    path('payment/<int:product_id>/', views.choose_payment, name='choose_payment'),
    path('payment/<int:product_id>/process/', views.process_payment, name='process_payment'),
    path('payment/', views.payment, name='payment'),
    path('shipping/<int:product_id>/', views.shipping, name='shipping'),
    path('transaction/history/', views.transaction_history, name='transaction_history'),
    path('transaction/history/<int:customer_id>/', views.transaction_history_customer, name='transaction_history_customer'),
    
    path('payment/verification/', views.payment_verification, name='payment_verification'),

    # Salesperson Interface URLs
    path('sales/dashboard/', views.sales_dashboard, name='sales_dashboard'),
    path('stores/', views.store_list, name='store_list'),
    path('stores/redirect', views.store_redirect, name='store_redirect'),
    path('stores/<int:store_id>/', views.store_page, name='store_page'),
    path('stores/delete/<int:store_id>/', views.delete_store, name='delete_store'),
    path("inventory/<int:store_id>", views.add_inventory, name = 'add_inventory'),

    # Store and Inventory Management URLs
    path('inventory/', views.inventory, name='inventory'),
    path('inventory/update/<int:product_id>/', views.update_inventory, name='update_inventory'),
    path('inventory/delete/<int:inventory_id>', views.delete_inventory, name='delete_inventory'),
    # Data Aggregation and Reporting URLs
    path('reports/sales/', views.sales_report, name='sales_report'),
    path('reports/category/', views.category_report, name='category_report'),
    path('reports/regions/', views.region_report, name='region_report'),
    path('reports/salesperson/', views.salesperson_report, name='salesperson_report'),
    path('reports/business/', views.business_product_report_search, name='business_product_report_search'),
    path('reports/business/<int:product_id>', views.business_product_report, name='business_product_report'),

    # Miscellaneous URLs
    path('ajax/', views.ajax),

    # Admin URL
    path('admin/', admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
