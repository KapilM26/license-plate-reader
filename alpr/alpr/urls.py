"""alpr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from app_alpr import views

router = routers.DefaultRouter()
router.register(r'data', views.appView, 'app_alpr')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.registerPage, name= "register"),
    path('login/', views.loginPage, name="login"),
    path('', include('app_alpr.urls')),
    path('api/', include(router.urls)),

    #remove after database
    #re_path(r'api/app_alpr/$', views.offender_list),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)
urlpatterns+=static(settings.PRED_URL, document_root=settings.PRED_ROOT)

