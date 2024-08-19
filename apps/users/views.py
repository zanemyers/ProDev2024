from django.shortcuts import render


def ProfilesView(request):
    return render(request, 'users/profiles.html')