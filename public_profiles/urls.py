from django.urls import path
from . import views
from .views import ProfileListView, ProfileDetailView

urlpatterns = [
    path('', ProfileListView.as_view(), name='classified-home'),# home route
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-details'),  
    path('about/', views.about, name='classified-about'), # about route, both are included in project (classified_ads) app
]


from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()