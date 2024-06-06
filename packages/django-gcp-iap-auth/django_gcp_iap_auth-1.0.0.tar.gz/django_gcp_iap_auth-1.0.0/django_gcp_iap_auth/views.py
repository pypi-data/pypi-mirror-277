from django.http import JsonResponse


def hello_world(request):
    name = request.user.username if request.user.is_authenticated else "unauthenticated user"
    return JsonResponse({"message": f"Hello {name}"})
