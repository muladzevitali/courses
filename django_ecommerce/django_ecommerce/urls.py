from django.conf.urls.static import (static, settings)
from django.contrib import admin
from django.urls import (path, include)

from . import views

urlpatterns = [
    path('de-admin/', admin.site.urls),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('', views.home, name='home'),
    path('store/', include('apps.store.urls')),
    path('cart/', include('apps.cart.urls')),
    path('auth/', include('apps.user.urls')),
    path('order/', include('apps.order.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
