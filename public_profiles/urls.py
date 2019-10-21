from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='classified-home'),  # home route
    path('about/', views.about, name='classified-about'), # about route, both are included in project (classified_ads) app
]


