from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from .models import AccessRecord, Topic, Webpage

# Create your views here.


class HomePageView(TemplateView):
    template_name = "first_app/home.html"


def about_view_page(request):
    my_dict = {"insert_me": "This is short information about my webpage!"}
    return render(request, "first_app/about.html", context=my_dict)


def index(request):
    webpages_list = AccessRecord.objects.order_by("date")
    date_dict = {
        "access_records": webpages_list,
    }
    return render(request, "first_app/index.html", context=date_dict)
