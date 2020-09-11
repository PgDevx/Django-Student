from django.urls import path
from Stud import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login',views.login, name="login"),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('changepaswd', views.change_paswd, name='chandepaswd'),
    path('display',views.display, name='display')
]