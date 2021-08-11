from django.urls import path
from . import views
from bffbook.views import home_view
urlpatterns = [
    path('', home_view, name='home-view'),
    path('register', views.register, name='register'),
    path('verify', views.verify, name='verify'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]
