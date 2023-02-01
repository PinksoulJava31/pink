from django.urls import path
from . import views

app_name='myweb'
urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('product view',views.productview,name='product view'),
    path('product list',views.Productlist,name='product list'),
    path('about',views.about,name='about'),
    path('logout',views.logout,name='logout')
]