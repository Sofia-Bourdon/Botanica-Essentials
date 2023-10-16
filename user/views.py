from django.shortcuts import render


def user(request):
    """ Display the user's profile. """

    template = 'users/user.html'
    context = {}

    return render(request, template, context)
