from django.urls import path
from . import views
from schoolviews import redirect_to_login
urlpatterns = [
    path('', redirect_to_login),
    path('s/', redirect_to_login),
    path('s/<slug:username>/', views.home, name='home'),
]