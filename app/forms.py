from django import forms


from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import TextInput, FileInput, URLInput, EmailInput, PasswordInput, NumberInput, DateInput, TimeInput, CheckboxInput, Select, RadioSelect, Textarea


from .models import User, Profile, Post


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
            'profile_pic': FileInput(attrs={'class': 'form-control'}),
            'bio': TextInput(attrs={'class': 'form-control', 'placeholder': 'Update Bio'}),
        }
        
        
class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')
        
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post', 'image']
        
        widgets ={
            'post': Textarea(attrs={'class': 'form-control', 'placeholder': 'What\'s up in your hood? ' }),
            'image': FileInput(attrs={'class': 'form-control'}),
        }