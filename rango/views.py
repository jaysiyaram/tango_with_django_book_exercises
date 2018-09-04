from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

def index(request):
    # context_dict = {'boldmessage': "This is a bold message to be published"}
    category_list = Category.objects.order_by('-likes')
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context_dict)
    #return HttpResponse("Rango says hey there world!")

def about(request):
    context_dict = {'notboldmessage': "This is being done to learn something small yet significant"}
    return render(request, 'rango/about.html', context_dict)
    #return HttpResponse("Rango says here is the about page")
