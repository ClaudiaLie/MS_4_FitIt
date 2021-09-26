from django.shortcuts import render


def gym_classes(request):
    """ Return the gym classes page """

    return render(request, 'gym_classes/gym_classes.html')


def body_building(request):
    """ Return the body building page """

    return render(request, 'gym_classes/body_building.html')


def dance(request):
    """ Return the dance page """

    return render(request, 'gym_classes/dance.html')


def yoga(request):
    """ Return the yoga page """

    return render(request, 'gym_classes/yoga.html')


