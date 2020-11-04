from django.urls import path

from . import views

urlpatterns = [
    path('register_action', views.register_action, name='register_action'),
    path('register', views.register_view, name='register'),
    path('update_action', views.update_action, name='update_action'),
    path('update', views.update_view, name='update'),
    path('logout', views.logout_action, name='logout'),
    path('home', views.home, name='home'),
    path('login_action', views.login_action, name='login_action'),
    path('', views.index, name='index'),
]
