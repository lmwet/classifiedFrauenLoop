"""classified_ads URL Configuration

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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from private_profiles import views as private_views


urlpatterns = [
    path('admin/', admin.site.urls),    # admin route
    path('register/', private_views.register, name='register'), # register route
    path('profiles_developer/', private_views.profiles_developer, name='profiles-developer'), # developers' profiles route
    path('login/', auth_views.LoginView.as_view(template_name='private_profiles/login.html'), name='login'), # template_name > to avoid default route in registration dir (that we do not have)
    path('logout/', auth_views.LogoutView.as_view(template_name='private_profiles/logout.html'), name='logout'),
    path('', include('public_profiles.urls')), # "inheriting" from public_profiles app, there is no urls.py in private_profiles!
]

if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
