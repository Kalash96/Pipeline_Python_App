from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. Here is a test of Azure!!!")

def add_numbers(x, y):
    return x + y