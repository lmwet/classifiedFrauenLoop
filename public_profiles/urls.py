from django.urls import path
from . import views
from .views import ProfileListView, ProfileDetailView, successView, emailView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.home, name='classified-home'),  # home route
    path('', ProfileListView.as_view(), name='classified-home'),# home route
    path('profile/<int:pk>/', ProfileDetailView.as_view() and emailView, name='profile-details'), 
    # added two views so that both appear on page HOWEVER data has disappeared and form is not there
    path('success/', successView, name='success'),
    path('about/', views.about, name='classified-about'), # about route, both are included in project (classified_ads) app
]

urlpatterns += staticfiles_urlpatterns()