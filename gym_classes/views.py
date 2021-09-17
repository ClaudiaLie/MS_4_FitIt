from django.shortcuts import render


def gym_classes(request):
    """ Return the gym classes page """

    return render(request, 'gym_classes/gym_classes.html')
