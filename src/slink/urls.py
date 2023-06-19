from django.contrib import admin
from django.urls import path, include

from slink.core.urls import urlpatterns as core_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include((core_urlpatterns, 'core'), namespace='core')),
]
