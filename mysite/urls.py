from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.conf.urls.static import static

admin.site.site_header = "Top Secret Area"

from shoestrap.views import (

    #shoestrap EXAMPLE VIEWS
    album_view,
    blog_view,
    carousel_view,
    checkout_view,
    cover_view,
    dashboard_view,
    floating_labels_view,
    grid_view,
    jumbotron_view,
    navbar_bottom_view,
    navbar_fixed_view,
    navbar_static_view,
    navbars_view,
    offcanvas_view,
    pricing_view,
    product_view,
    sign_in_view,
    starter_template_view,
    sticky_footer_navbar_view,
    sticky_footer_view,

    # _view,
    # _view,
    # _view,
    # _view,

)

urlpatterns = [
    #DJANGO BASE URLS
    path('admin/', admin.site.urls),

    #shoestrap BASE URLS
    path('', include('shoestrap.urls')),

    #shoestrap BASE URLS
    path("album/", view=album_view, name="album"),
    path("blog/", view=blog_view, name="blog"),
    path("carousel/", view=carousel_view, name="carousel"),
    path("checkout/", view=checkout_view, name="checkout"),
    path("cover/", view=cover_view, name="cover"),
    path("dashboard/", view=dashboard_view, name="dashboard"),
    path("floating_labels/", view=floating_labels_view, name="floating_labels"),
    path("grid/", view=grid_view, name="grid"),
    path("jumbotron/", view=jumbotron_view, name="jumbotron"),
    path("navbar_bottom/", view=navbar_bottom_view, name="navbar_bottom"),
    path("navbar_fixed/", view=navbar_fixed_view, name="navbar_fixed"),
    path("navbar_static/", view=navbar_static_view, name="navbar_static"),
    path("navbars/", view=navbars_view, name="navbars"),
    path("offcanvas/", view=offcanvas_view, name="offcanvas"),
    path("pricing/", view=pricing_view, name="pricing"),
    path("product/", view=product_view, name="product"),
    path("sign_in/", view=sign_in_view, name="sign_in"),
    path("starter_template/", view=starter_template_view, name="starter_template"),
    path("sticky_footer_navbar/", view=sticky_footer_navbar_view, name="sticky_footer_navbar"),
    path("sticky_footer/", view=sticky_footer_view, name="sticky_footer"),

    # path("/", view=_view, name=""),
    # path("/", view=_view, name=""),
    # path("/", view=_view, name=""),
    # path("/", view=_view, name=""),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


