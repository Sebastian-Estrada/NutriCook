from django.urls import path
from .views import (
    Login, Logout, UsersList, ModifyUser,
    ResetPassword, Deactivate, Activate, Register
)

app_name = 'users'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('list/', UsersList.as_view(), name='user_list'),
    path('update/<int:pk>/', ModifyUser.as_view(), name='user_update'),
    path('reset-password/<int:pk>/', ResetPassword.as_view(), name='reset_password'),
    path('deactivate/<int:user_id>/', Deactivate.as_view(), name='deactivate'),
    path('activate/<int:user_id>/', Activate.as_view(), name='activate'),
    path('register/', Register.as_view(), name='register'),
]
