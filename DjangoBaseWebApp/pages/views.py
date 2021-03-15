from django.shortcuts import render, get_object_or_404
from .models import Page


def index(request, pagename):
    # return HttpResponse("<h1> VC Healy Home page</h1>")
    # return render(request, "base.html")
    # return render(request, "pages/page.html")

    pagename = "/" + pagename
    # pg = Page.objects.get(permalink=pagename)
    pg = get_object_or_404(Page, permalink=pagename)
    context = {
        "title": pg.title,
        "content": pg.bodytext,
        "last updated": pg.update_date,
        "page_list": Page.objects.all(),
    }
    # assert False
    return render(request, "pages/page.html", context)
