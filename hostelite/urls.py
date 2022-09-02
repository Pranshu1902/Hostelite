"""hostelite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from rest_framework import routers
from django.conf import settings
from rest_framework.authtoken import views

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from hostel.apiViews import ComplaintViewSet, HealthReportViewSet, LeaveRequestViewSet, RoomCleaningViewSet

router = routers.SimpleRouter(trailing_slash=True)

router.register("leave", LeaveRequestViewSet, basename="Leave request")
router.register("complaint", ComplaintViewSet, basename="Complaint")
router.register("health", HealthReportViewSet, basename="health report")
router.register("cleaning", RoomCleaningViewSet, basename="room cleaning")

urlpatterns = [
    path('api/', SpectacularAPIView.as_view(), name="schema"),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('api-token-auth/', views.obtain_auth_token),

    path('admin/', admin.site.urls),
] + router.urls + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
