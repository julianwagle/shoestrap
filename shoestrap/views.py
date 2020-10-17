from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout

def index(request):
    return HttpResponse("Hello, world. You're at the shoestrap index.")

#shoestrap VIEWS 

def album_view(request, *args, **kwargs):
	return render(request, "shoestrap/album.html")

def blog_view(request, *args, **kwargs):
	return render(request, "shoestrap/blog.html")

def carousel_view(request, *args, **kwargs):
	return render(request, "shoestrap/carousel.html")

def checkout_view(request, *args, **kwargs):
	return render(request, "shoestrap/checkout.html")   

def cover_view(request, *args, **kwargs):
	return render(request, "shoestrap/cover.html")

def dashboard_view(request, *args, **kwargs):
	return render(request, "shoestrap/dashboard.html")

def floating_labels_view(request, *args, **kwargs):
	return render(request, "shoestrap/floating_labels.html")

def grid_view(request, *args, **kwargs):
	return render(request, "shoestrap/grid.html")   

def jumbotron_view(request, *args, **kwargs):
	return render(request, "shoestrap/jumbotron.html")

def navbar_bottom_view(request, *args, **kwargs):
	return render(request, "shoestrap/navbar_bottom.html")

def navbar_fixed_view(request, *args, **kwargs):
	return render(request, "shoestrap/navbar_fixed.html")

def navbar_static_view(request, *args, **kwargs):
	return render(request, "shoestrap/navbar_static.html")    

def navbars_view(request, *args, **kwargs):
	return render(request, "shoestrap/navbars.html")

def offcanvas_view(request, *args, **kwargs):
	return render(request, "shoestrap/offcanvas.html")

def pricing_view(request, *args, **kwargs):
	return render(request, "shoestrap/pricing.html")

def product_view(request, *args, **kwargs):
	return render(request, "shoestrap/product.html")

def sign_in_view(request, *args, **kwargs):
	return render(request, "shoestrap/sign_in.html")   

def starter_template_view(request, *args, **kwargs):
	return render(request, "shoestrap/starter_template.html")

def sticky_footer_navbar_view(request, *args, **kwargs):
	return render(request, "shoestrap/sticky_footer_navbar.html")

def sticky_footer_view(request, *args, **kwargs):
	return render(request, "shoestrap/sticky_footer.html")

# def _view(request, *args, **kwargs):
# 	return render(request, "shoestrap/.html")   

# def _view(request, *args, **kwargs):
# 	return render(request, "shoestrap/.html")

# def _view(request, *args, **kwargs):
# 	return render(request, "shoestrap/.html")

# def _view(request, *args, **kwargs):
# 	return render(request, "shoestrap/.html")

# def _view(request, *args, **kwargs):
# 	return render(request, "shoestrap/.html")          