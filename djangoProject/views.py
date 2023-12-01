from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello World")


from django.shortcuts import render


def runoob(request):
    context = {}
    context['hello'] = 'Hello World!'
    context['try'] = 'Hello try!'
    return render(request, 'runoob.html', context)