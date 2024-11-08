from django.shortcuts import render
from django.http import HttpResponse
from visits.models import PageVisit


def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    my_title = "My Home Page"
    my_html = "home.html"
    my_context = {
        "page_title": my_title,
        "total_visits_count": qs.count(),
        "page_visits_count": page_qs.count(),
        "percent_visited": (
            (page_qs.count() / qs.count()) * 100 if qs.count() > 0 else 0
        ),
    }
    PageVisit.objects.create(path=request.path)
    return render(request, my_html, my_context)
    return HttpResponse("Welcome to the Home Page!")
