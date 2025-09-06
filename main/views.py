from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app' : 'PreBuy',
        'name': 'Kalfin Jefwin Setiawan Gultom',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)