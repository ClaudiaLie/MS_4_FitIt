from django.shortcuts import render, redirect


def prices(request):
    """ Return the prices page """
    return render(request, 'prices/prices.html')


def view_bag(request):
    """ Render the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add to the shopping bag """

    redirect_url = request.POST.get('redirect_url')

    bag = request.session.get('bag', {})

    request.session['bag'] = bag
    return redirect(redirect_url)
