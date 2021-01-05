from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout

def home_view(request, *args, **kwargs):
	return render(request, "examples/home.html")

def album_view(request, *args, **kwargs):
	return render(request, "examples/album.html")

def blog_view(request, *args, **kwargs):
	return render(request, "examples/blog.html")

def carousel_view(request, *args, **kwargs):
	return render(request, "examples/carousel.html")

def checkout_view(request, *args, **kwargs):
	return render(request, "examples/checkout.html")   

def cover_view(request, *args, **kwargs):
	return render(request, "examples/cover.html")

def dashboard_view(request, *args, **kwargs):
	return render(request, "examples/dashboard.html")

def floating_labels_view(request, *args, **kwargs):
	return render(request, "examples/floating_labels.html")

def jumbotron_view(request, *args, **kwargs):
	return render(request, "examples/jumbotron.html")

def offcanvas_view(request, *args, **kwargs):
	return render(request, "examples/offcanvas.html")

def pricing_view(request, *args, **kwargs):
	return render(request, "examples/pricing.html")

def product_view(request, *args, **kwargs):
	return render(request, "examples/product.html")

def sign_in_view(request, *args, **kwargs):
	return render(request, "examples/sign_in.html")   
