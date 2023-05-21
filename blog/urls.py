from django.contrib import admin
from django.urls import path, include

# from django.views.generic import RedirectView  # ME - MDN dj tuto
from django.contrib.sitemaps.views import sitemap
from blog_app.sitemaps import PostSitemap

sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    path("blog/", include("blog_app.urls", namespace="blog")),
    # path(
    #     "sitemap.xml",
    #     sitemap,
    #     {"sitemaps": sitemaps},
    #     name="django.contrib.sitemaps.views.sitemap",
    # ),
    path("admin/", admin.site.urls),
    # path('', RedirectView.as_view(url='blog/', permanent=True)),  # ME - MDN dj tuto
    # path('__debug__/', include('debug_toolbar.urls')),
]
