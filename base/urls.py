from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.Home,name='home'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('signup/',views.signup,name="signup"),
    path('shop/',views.shop,name="shop"),
    path('mobiles/',views.mobiles,name="mobile"),
    path('televisions/',views.televisions,name="televisons"),
    path('tabs/',views.tabs,name="tabs"),
    path('headsets/',views.headsets,name="headsets"),
    path('accessories/',views.accessories,name="accessories"),
    path('watches/',views.watches,name="watches"),
    path('laptops/',views.laptops,name="laptop"),
    path('adminlte/',views.adminlte,name='adminlte'),
    path('buy/',views.buy,name='buy'),
    path('cart/',views.cart,name='cart'),
    
    #path('shop/<int:id>',views.item,name='item'),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)