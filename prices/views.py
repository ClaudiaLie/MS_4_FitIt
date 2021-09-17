from django.shortcuts import render


def prices(request):
    """ Return the prices page """
    return render(request, 'prices/prices.html')
