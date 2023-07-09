from django.contrib import admin
from django.urls import path, include
from .settings import MEDIA_URL, MEDIA_ROOT, STATIC_URL, STATIC_ROOT
from django.conf.urls.static import static
from . import swagger

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('to_do_list.urls')),
    path('api/v1/', include('users.urls')),
    path('api/v1/', include('profiles.urls'))
]
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
urlpatterns += swagger.urlpatterns