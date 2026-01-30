from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to MyWeb! Python and Django application.")
