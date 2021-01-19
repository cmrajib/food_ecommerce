
from django.contrib import admin
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('UserRegistration.urls')),
    path('', include('home.urls')),
    path('shop/', include('shop.urls')),
    path('order/', include('order.urls')),
    path('payment/', include('payment.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


