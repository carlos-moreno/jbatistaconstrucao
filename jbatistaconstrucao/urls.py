from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from jbatistaconstrucao import settings
from jbatistaconstrucao.core.views import home, portfolio_detail

urlpatterns = [
    path("", home, name="home"),
    path("portfolio/<int:pk>/", portfolio_detail, name="portfolio_detail"),
    path('froala_editor/', include('froala_editor.urls')),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


