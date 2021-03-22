from django.contrib import admin
from django.urls import path, include
import blog.views
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    path('blog/<int:blog_id>', blog.views.detail, name="detail"),
    path('add/', blog.views.add, name="add"),
    
    path('accounts/', include('accounts.urls')),		# url 상속 : accounts/~~의 URL은 accounts app폴더의 urls.py로 이동

    path('create/', blog.views.create, name="create"),
]
