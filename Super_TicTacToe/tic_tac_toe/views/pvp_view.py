from django.shortcuts import render


# Create your views here.
def pvp(request):
    return render(request, 'pvp.html')
