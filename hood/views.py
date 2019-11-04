from django.shortcuts import render, redirect
from django.http  import HttpResponse, Http404, HttpResponseRedirect
from .models import Business, NeighbourHood, Profile
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, NewBusinessForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    business = Business.objects.all()
    current_user = request.user
    ngbrhd = NeighbourHood.objects.all()
    user_profile = Profile.objects.all()
    profile = Profile.objects.filter(id=current_user.id).first()
    return render(request, 'index.html',{'business':business,'ngbrhd':ngbrhd, 'profile':profile, 'user_profile':user_profile})

@login_required(login_url='/accounts/login/')
def neighborhood(request):
    neighbor = NeighbourHood.objects.all()
    buzz = Business.objects.all()
    return render(request, 'neighborhood.html', {'buzz':buzz})

def search_results(request):
    '''
    a view to do the search the image by category
    '''
    if 'image' in request.GET and request.GET["image"]:
        search = request.GET.get('image')
        searched = Image.search_image(search)
        message = f"{search}"
        
        return render(request,"all-app/search.html", {"message":message, "images":searched})

    else:
        message = 'You have not searched for any image'
        return render(request, 'all-app/search.html',{"message":message}) 

@login_required(login_url='/accounts/login')    
def business(request,id):
    try:
        buzz= Business.objects.get(id=id)
    except DoesNotExist:
        raise Http404
    return render(request, 'index.html',{'buzz':buzz})

@login_required(login_url='/accounts/login') 
def new_business(request):
    current_user = request.user 
    if request.method == 'POST':
        form = NewBusinessForm(request.POST, request.FILES)
        if form.is_valid():
            buzz = form.save(commit=False)
            buzz.user = current_user
            buzz.save()
        return redirect('welcome')
    else:
        form = NewBusinessForm()
    return render (request, 'new_business.html', {"form":form})

@login_required(login_url='/accounts/login')    
def profile(request):
    current_user = request.user
    picture = Profile.objects.filter(user=current_user).all()
    profiles = Profile.objects.filter(user=current_user).first()
    return render(request, 'profile.html',{'profiles':profiles})

@login_required(login_url='/accounts/login')
def new_profile(request):
    current_user = request.user 
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('welcome')
    else:
        form = ProfileForm()
    return render (request, 'new_profile.html', {"form":form})
