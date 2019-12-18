from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class ClassifiedRegistrationForm(UserCreationForm):
    username = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Username'}))  # creating fields in addition to in-built User fields 
    email = forms.EmailField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Email'}))     # all fields habe a placeholder, label (above field) remains empty
    password1 = forms.CharField(label='', 
                    widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='', 
                    widget=forms.PasswordInput(attrs={'placeholder': 'Enter the same password again'}))
        

    class Meta:
        model = User # our model is based on django's User model
        fields = ['username', 'email', 'password1', 'password2'] # succession of fields in order of appearance on site



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ['username', 'email']


PROGRAMMING_LANGUAGES_CHOICES = [('Python', 'Python'), ('Ruby', 'Ruby'), ('Go(lang)', 'Go(lang)'), ('Javascript', 'Javascript'), ('Java','Java'), ('PHP', 'PHP')]
class ProfileUpdateForm(forms.ModelForm):
    programming_languages = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=PROGRAMMING_LANGUAGES_CHOICES,)

    class Meta():
    
        model = Profile
        fields = ['skills', 'languages', 'likes', 'dislikes', 'github', 'programming_languages']