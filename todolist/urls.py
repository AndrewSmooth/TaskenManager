from django.urls import path, include
from .views import all_tasks, profile
from users import views as user_views


app_name = "todolist"

urlpatterns = [  
    path('accounts/profile/delete/', user_views.DeleteUserView.as_view(), name='profile_delete'),
    path ('accounts/profile/change/', user_views.ChangeUserlnfoView.as_view(), name='profile_change'),
    path ('accounts/profile/', profile, name='profile'),
    path('accounts/logout', user_views.TodoLogoutView.as_view(), name='logout' ),
    path ('accounts/passwords/change/', user_views.TodoPasswordChangeView.as_view(), name='password_change'),
    path ('password-reset/', user_views.send_instruction, name='password_reset'),
    path('password-reset/<str:sign>/', user_views.SetNewPasswordView, name='set_new_password'),
    
    path('accounts/register/activate/<str:sign>/', user_views.user_activate, name='register_activate'),
    path ('accounts/register/done/', user_views.RegisterDoneView.as_view(), name='register_done'),
    path ('accounts/register/', user_views.RegisterUserView.as_view(), name='register'),
    path('accounts/login', user_views.TodoLoginView.as_view(), name='login' ),
    path('accounts/all-tasks', all_tasks, name='all-tasks'),
    path('', all_tasks, name='start'),  
]
