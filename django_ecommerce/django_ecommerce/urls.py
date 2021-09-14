from django.conf.urls.static import (static, settings)
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.home, name='home')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
