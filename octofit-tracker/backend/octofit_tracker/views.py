from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the Octofit Tracker API!",
        "documentation": "https://literate-fiesta-576g65jr4wf57q-8000.app.github.dev",
    })
