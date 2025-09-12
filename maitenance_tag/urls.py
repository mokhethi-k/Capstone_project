"""
URL configuration for maitenance_tag project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from users.views import UserViewSet, ProfileViewSet, RegisterView

from rest_framework.routers import DefaultRouter
from tags.views import RepairTagViewSet
from actions.views import RepairTagActionViewSet
from tags.views import dashboard_stats

router = DefaultRouter()
router.register(r'users', UserViewSet, basename="user")
router.register(r'profiles', ProfileViewSet, basename="profile")
router.register(r'tags', RepairTagViewSet, basename="repairtag")
router.register(r'actions', RepairTagActionViewSet, basename="repairtagaction")


auth_api_urls = [
    path(r'', include('rest_framework.urls')),

]

api_url_patterns = [
    path(r'auth/', include(auth_api_urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path(r'', include(router.urls)),
    path('dashboard/', dashboard_stats, name="dashboard"),
    
]


urlpatterns = [
    path('api/', include(api_url_patterns)),
    path('admin/', admin.site.urls),
    

]
