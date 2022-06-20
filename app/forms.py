from django import forms


from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import TextInput, FileInput, NumberInput, Textarea


from .models import User, Profile, Post, Neighborhood, SocialAmenities, Business


class SocialAmenitiesForm(forms.ModelForm):
    class Meta:
        model = SocialAmenities
        fields = ('name', 'email', 'description', 'location','neighborhood')
        
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'location': TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
        }


class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields = ('name', 'location', 'occupants_count')
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your neighborhood name'
            }),
            'location': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your neighborhood location'
            }),
            'occupants_count': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your neighborhood occupants count'
            }),
        }


class SignupForm(UserCreationForm):
    full_name = forms.CharField(max_length=230)
    mobile = forms.CharField(max_length=230, widget=forms.TextInput(attrs={'type': 'number'}))
    address = forms.CharField(max_length=230)
    
    class Meta:
        model = User
        fields = ('full_name','mobile','address','password1', 'password2')
    

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio']
        
        widgets ={
            'profile_pic': FileInput(attrs={'class': 'form-control', 'placeholder': 'Profile Picture'}),
            'bio': TextInput(attrs={'class': 'form-control', 'placeholder': 'Update Bio'}),
        }
        
        
class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('email',)
        
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post', 'image']
        
        widgets ={
            'post': Textarea(attrs={'class': 'form-control', 'placeholder': 'What\'s up in your hood? ' }),
            'image': FileInput(attrs={'class': 'form-control'}),
        }
        
        
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'email', 'description', 'neighborhood']
        
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }