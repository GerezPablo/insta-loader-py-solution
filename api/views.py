from django.http import HttpResponse
from api.InstaLoaderAPI import InstaLoaderAPI


def root(request):
    q = request.GET.get('q', None)

    return HttpResponse(f"It's alive! {q if q != None else ''}")


def downloadPost(request, shortCode):
    username = request.GET.get('username', None)
    password = request.GET.get('password', None)

    try:
        instance = InstaLoaderAPI(username, password)
        instance.dowloadPostFromShortCode(shortCode)

        return HttpResponse("Downloading...")
    except Exception as error:
        return HttpResponse(f"Se rompió: {error}")
