"""inlaks_db URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from inlaks_app import views
from users import views as userV
from django.contrib.auth import views as authV
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

router = routers.DefaultRouter()
router.register("ATM", views.ATMView)
router.register("Service", views.ServiceView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('WebService/', include(router.urls)),
    path('home/', include('inlaks_app.urls')),
    path('', userV.register, name='register-home'),
    path('register/', userV.register, name='register'),
    path('login/', authV.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/', authV.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('password-reset/', authV.PasswordResetView.as_view(template_name='users/password-reset.html'),name='password-reset'),
    path('password-reset/done', authV.PasswordResetDoneView.as_view(template_name='users/password-reset_done.html'),name='password_reset_done'),
    path('password-reset-done/<uidb64>/<token>', authV.PasswordResetConfirmView.as_view(template_name='users/password-reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset/complete', authV.PasswordResetCompleteView.as_view(template_name='users/password-reset_complete.html'),name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)