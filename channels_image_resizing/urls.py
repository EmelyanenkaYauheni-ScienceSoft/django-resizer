from django.conf.urls import url, include
from django.contrib import admin
from resizers import views
from rest_framework.routers import DefaultRouter
from django.views.static import serve
from django.conf import settings


router = DefaultRouter()
router.register(r'images', views.ImageViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^statistics/', views.statistics),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
