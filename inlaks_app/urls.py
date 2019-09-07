from django.urls import path
from . import views
from users import views as userViews
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', views.home, name='home'),
    path('profile/', userViews.profile, name='profile'),
    path('chart/', views.atm, name='chart'),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)