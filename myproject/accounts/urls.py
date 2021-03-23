from django.urls import path, include
from . import views

urlpatterns = [
	path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name="logout"),
    
    # 소셜 로그인 관련
    path('google/', include('allauth.urls')),
]