from django.contrib import admin
from django.urls import path, include

# from django.views.generic import RedirectView  # ME - MDN dj tuto
from django.contrib.sitemaps.views import sitemap
from blog_app.sitemaps import PostSitemap
from django.conf import settings
from django.conf.urls.static import static


sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    path("", include("blog_app.urls", namespace="blog")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("admin/", admin.site.urls),
    # path('', RedirectView.as_view(url='blog/', permanent=True)),  # ME - MDN dj tuto
    # path('__debug__/', include('debug_toolbar.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
