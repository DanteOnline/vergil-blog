from django.urls import path
from .views import BlogUserCreateView, logout, LoginFormView

app_name = 'user_app'

urlpatterns = [
    path('login/', LoginFormView.as_view(), name='login'),
    path('registration/', BlogUserCreateView.as_view(), name='registration'),
    path('logout/', logout, name='logout'),
]
