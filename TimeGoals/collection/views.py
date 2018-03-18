from django.shortcuts import render
from collection.models import Profile

# Create your views here.
def index(request):
    #define a variable
    profiles = Profile.objects.all().order_by('name')
    return render(request, 'index.html', {
        'profiles': profiles,
    })

def profile_detail(request, slug):
    #grab the object...
    profile = Profile.objects.get(slug=slug)
    #and pass to the template
    return render(request, 'profiles/profile_detail.html', {
        'profile': profile,
    })
