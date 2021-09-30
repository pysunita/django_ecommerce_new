from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    context = {
        "title": "Hello World",
        "content":"This is home page"
    }
    return render(request, "home_page.html", context)


def about_page(request):
    return render(request, "home_about.html", {})


def contact_page(request):
    return render(request, "contact_page.html", {})
