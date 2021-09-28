from django.conf.urls.static import (static, settings)
from django.contrib import admin
from django.urls import (path, include)

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('store/', include('apps.store.urls')),
    path('cart/', include('apps.cart.urls')),
    path('auth/', include('apps.user.urls')),
    path('order/', include('apps.order.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
