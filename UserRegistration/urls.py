

from django.urls import path
from . import views

app_name = 'UserRegistration'

urlpatterns = [
    path('',views.home,name='home'),
    # path('signup1/', views.sign_up1, name='signup1'),
    # path('login1/', views.login_user1, name='login1'),
    path('logout/', views.logout_user, name='logout'),
    # path('profile/', views.user_profile, name='profile'),

    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login_user, name='login'),
    path('changepassword/', views.change_password, name='change_password'),
    # path('forgot-password/',views.forgot_password, name='forgot_password'),
]










#  http://localhost:8000/accounts/signup/
# http://localhost:8000/accounts/login/
# http://localhost:8000/accounts/logout/
# http://localhost:8000/profile
# http://localhost:8000/profile/password
