from django.urls import path

from . import views

urlpatterns = [
    path('main', views.main, name='main'),
    path('UserRegistration', views.UserRegistration, name='UserRegistration'),
    path('UserLogin',views.UserLogin,name='UserLogin'),
    path('ShowUserinformation',views.ShowUserinformation,name='ShowUserinformation'),
    path('editProfile',views.editProfile,name='editProfile'),
    path('UserLogOut', views.UserLogOut, name='UserLogOut'),
    path('ProductInformation', views.ProductInformation, name='ProductInformation'),
    path('AddProductToCart', views.AddProductToCart, name='AddProductToCart'),
    path('getAllOrderByUsername', views.getAllOrderByUsername, name='getAllOrderByUsername'),
    path('CheckOut', views.CheckOut, name='CheckOut'),
    path('PlaceOrder', views.PlaceOrder, name='PlaceOrder'),
    path('searchByCategory', views.searchByCategory, name='searchByCategory'),
]