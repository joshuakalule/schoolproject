from django.urls import path
from . import views
urlpatterns = [
    path('', views.redirect_to_login),
    path('s/', views.redirect_to_login),
    path('s/<slug:username>/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='user_login')
]