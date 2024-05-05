from django.contrib import admin
from django.urls import path
from welcome import views as welcome_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome_views.welcome_user, name='welcome'),
]
