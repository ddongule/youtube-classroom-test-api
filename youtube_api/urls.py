from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers
from videos.views import VideoViewSet

router = routers.DefaultRouter()
router.register('videos', VideoViewSet)

urlpatterns = [ url(r'^admin/', admin.site.urls), url(r'^',include(router.urls)), ]
