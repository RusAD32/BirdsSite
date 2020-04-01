from django.shortcuts import render


# Create your views here.
def index_view(request):
    return render(request, "index.html")


def strizh_view(request):
    return render(request, "strizhi.html")


def contacts_view(request):
    return render(request, "info_for.html")


def black_list(request):
    return render(request, "black_list.html")


def section_1(request):
    return render(request, "section_1.html")


def section_2(request):
    return render(request, "section_2.html")


def section_3(request):
    return render(request, "section_3.html")


def section_4(request):
    return render(request, "section_4.html")


def section_5(request):
    return render(request, "section_5.html")


def section_6(request):
    return render(request, "section_6.html")


def section_7(request):
    return render(request, "section_7.html")


def section_8(request):
    return render(request, "section_8.html")


def section_9(request):
    return render(request, "section_1.html")


def section_10(request):
    return render(request, "section_10.html")


def section_11(request):
    return render(request, "section_11.html")


def opredelitel(request):
    return render(request, "opredelitel.html")


def letnost(request):
    return render(request, "section_10_1.html")


def section_1_4(request):
    return render(request, "section_1_4.html")


def section_contacts(request):
    return render(request, "contacts.html")
