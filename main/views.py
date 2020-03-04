from django.shortcuts import render


# Create your views here.
def index_view(request):
    return render(request, "index.html")


def strizh_view(request):
    return render(request, "strizhi.html")


def contacts_view(request):
    return render(request, "contacts.html")