from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),

    re_path('inventory/', include('product.urls')),

    path('accounts/', include('django.contrib.auth.urls')),

    re_path('', include('user.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
