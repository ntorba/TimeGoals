from django.shortcuts import render

# Create your views here.
def index(request):
    #define a variable
    number = 6
    #this is your new views
    return render(request, 'index.html', {
        'number': number,
    })
