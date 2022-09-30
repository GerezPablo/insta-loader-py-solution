from django.http import HttpResponse, request
from api.InstaLoaderAPI import InstaLoaderAPI

def root(request):
    q = request.GET.get('q', None)

    return HttpResponse("It's alive!\n" + q)


def downloadPost(request, shortCode):
    username = request.GET.get('username', None)
    password = request.GET.get('password', None)

    try:
        instance = InstaLoaderAPI(username, password)
        instance.dowloadPostFromShortCode(shortCode)

        return HttpResponse("Downloading...")
    except Exception as error:
        return HttpResponse(f"Se rompió: {error}")

