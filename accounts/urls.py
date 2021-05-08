from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout')
]
