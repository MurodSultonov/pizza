from django.shortcuts import render
from pages.models import MainScrollModel, Menu

def home_page_view(request):
    scrolls = MainScrollModel.objects.all().order_by('-pk')
    menu = Menu.objects.all().order_by('-pk')
    context = {
        'scrolls': scrolls,
        'menues': menu
    }
    return render(request, 'index.html', context)