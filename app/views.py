from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.urls import reverse

from django.db.models import Q
from itertools import chain

from django.contrib.auth.decorators import login_required

from .models import Neighborhood, User, Profile, Business, Post, SocialAmenities
from .forms import UpdateProfileForm, SignupForm, PostForm, UpdateUserForm

# Create your views here.

def index(request):
    return render(request, 'main/index.html')


@login_required(login_url='/accounts/login/')
def home(request, neighborhood_id):
    neighborhood = get_object_or_404(Neighborhood, pk=neighborhood_id)
    posts = Post.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home', neighborhood.id)
            
    else:
        form = PostForm()
        
    params = {
        'posts': posts,
        'form': form,
        'neighborhood': neighborhood,
    }
    return render(request, 'main/home.html', params)


@login_required(login_url='/accounts/login/')
def profile(request, username):
    user = get_object_or_404(User, username=username)
    
    context = {
        'user': user,
       
    }
    
    return render(request, 'profile/profile.html', context)


@login_required(login_url='/accounts/login/')
def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    
    context = {
        'user': user,
    }

    return render(request, 'profile/other_user.html', context)

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'query' in request.GET and request.GET['query']:
        search_term = request.GET.get('query')
        # searched_query = Neighborhood.find_neighborhood(search_term)
        searched_business = Business.objects.filter(name__icontains=search_term)
        searched_post = Post.objects.filter(post__icontains=search_term)
        searched_social = SocialAmenities.objects.filter(name__icontains=search_term)
        
        message = f"{search_term, searched_business, searched_post, searched_social}"
        
        results = chain(searched_business, searched_post,searched_social)
        
        params = {
            'message': message,
            'results': results,
            'businesses': searched_business,
            'posts': searched_post,
            'social_amenities': searched_social
        }
        
        return render(request, 'search/search.html', params)
    else:
        message = "You haven't searched for any term"
        return render(request, 'search/search.html', {"message": message})
    
    
@login_required(login_url='/accounts/login/')
def updateprofile(request, username):
    # user = User.objects.get(username=username)
    user = get_object_or_404(User, username=username)
    
    if request.method == 'POST':
        user_form=UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid()  and user_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile', user.username)
    
    else:
        profile_form = UpdateProfileForm()
        user_form = UpdateUserForm()
        
    params = {
        'form': profile_form,
        'user_form': user_form,
    }

    return render(request, 'profile/updateprofile.html',params)
        
       
@login_required(login_url='/accounts/login/')               
def neighborhood(request):
    neighborhoods = Neighborhood.objects.all()
    
    params = {
        'neighborhoods': neighborhoods
    }
    return render(request, 'main/select_hood.html', params)



@login_required(login_url='/accounts/login/')
def businesses(request, neighborhood_id):
    neighborhood = get_object_or_404(Neighborhood, pk=neighborhood_id)
    businesses = Business.objects.filter(neighborhood=neighborhood)
    
    params = {
        'businesses': businesses
    }
    return render(request, 'main/businesses.html', params)


def social_amenities(request, neighborhood_id):
    neighborhood = get_object_or_404(Neighborhood, pk=neighborhood_id)
    amenities=SocialAmenities.objects.filter(neighborhood=neighborhood)
    
    params = {
        'amenities': amenities
    }
    return render(request, 'main/social_amenities.html', params)


