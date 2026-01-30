# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Welcome to MyWeb! Python and Django application.")


from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')
