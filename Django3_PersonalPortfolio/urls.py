
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from portfolio import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from portfolio.views import contact, success

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('contact/', contact,name='contact'),
    path('success/', success,name='success'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
