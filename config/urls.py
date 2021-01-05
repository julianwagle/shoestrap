from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.site.site_header = "Top Secret Area"

from examples.views import (
    home_view,
    album_view,
    blog_view,
    carousel_view,
    checkout_view,
    cover_view,
    dashboard_view,
    floating_labels_view,
    jumbotron_view,
    offcanvas_view,
    pricing_view,
    product_view,
    sign_in_view,
)


urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path("about/", TemplateView.as_view(template_name="pages/about.html"), name="about"),

    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),

    # User management
    path("users/", include("base.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),

    # Example page urls go here

    path("example_home/", view=home_view, name="example_home"),
    path("example_album/", view=album_view, name="example_album"),
    path("example_blog/", view=blog_view, name="example_blog"),
    path("example_carousel/", view=carousel_view, name="example_carousel"),
    path("example_checkout/", view=checkout_view, name="example_checkout"),
    path("example_cover/", view=cover_view, name="example_cover"),
    path("example_dashboard/", view=dashboard_view, name="example_dashboard"),
    path("example_floating_labels/", view=floating_labels_view, name="example_floating_labels"),
    path("example_jumbotron/", view=jumbotron_view, name="example_jumbotron"),
    path("example_offcanvas/", view=offcanvas_view, name="example_offcanvas"),
    path("example_pricing/", view=pricing_view, name="example_pricing"),
    path("example_product/", view=product_view, name="example_product"),
    path("example_sign_in/", view=sign_in_view, name="example_sign_in"),

    # Your stuff: custom urls includes go here

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
