from django.urls import path
from .views import *

urlpatterns = [
    path('',home_view,name='home'),
    path('login',login_view,name='login'),
    path('logout',logout_view,name='login'),
    path('choice',choice_view,name='choice'),
    path('register',register_view,name='register'),
    path('update',update_view,name='update'),
]