from django.shortcuts import render, redirect
from collection.forms import ProfileForm
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

def edit_profile(request, slug):
    #grab the object
    profile = Profile.objects.get(slug=slug)
    #set the form we're using..
    form_class = ProfileForm
    #if we're coming to this view from a submitted form,
    if request.method == 'POST':
        #grab the data from the submitted form
        form = form_class(data=request.POST, instance=profile)
        if form.is_valid():
            #save the new data
            form.save()
            return redirect('profile_detail', slug=profile.slug)
    else:
        form = form_class(instance = profile)

    #and render the template
    return render(request, 'profiles/edit_profile.html', {
        'profile': profile,
        'form': form,
    })
