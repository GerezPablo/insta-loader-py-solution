from django.http import HttpResponse
from InstaLoaderAPI import InstaLoaderAPI


def root(request):
    return HttpResponse("It's alive!")


def downloadPost(request, shortCode):
    InstaLoaderAPI('instagram').dowloadPostFromShortCode(shortCode)
    return HttpResponse("Downloading")
