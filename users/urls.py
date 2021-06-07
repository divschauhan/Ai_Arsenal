from django.urls import path, include
from .views import dashboard, register, index

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('register/',register, name='register'),
    path('',index,name='index')

]