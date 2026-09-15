from django.conf.urls.static import static
from django.urls import path
from store import views
from django.conf import settings


urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('register/',views.register,name='register'),
    path('loginn/',views.loginn,name='loginn'),
    path('logoutt/',views.logoutt,name='logoutt'),
    path('product/',views.product,name='product'),
    # path('category/<int:id>/',views.category_product,name='category'),
    # path("category/", views.category_product, name="All_products"),
    path("prooduct_detail/<int:id>/", views.product_detail, name="product_detail"),
    path("add_to_cart/<int:id>/", views.add_to_cart, name="add_to_cart"),
    path("remove_cartItem/<int:id>/", views.remove_cartItem, name="remove_cartItem"),
    path("view_cart/", views.view_cart, name="view_cart"),
    path("contact/", views.contact, name="contact"),
    path("increase_q/<int:id>/", views.increase_q, name="increase_q"),
    path("decrease_q/<int:id>/", views.decrease_q, name="decrease_q"),
    path("checkout/", views.checkout, name="checkout"),
    path("success/<int:order_id>/", views.order_success, name="success"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
    