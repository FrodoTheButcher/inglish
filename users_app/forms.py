from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','first_name','last_name','password1','password2','username']

    def __init__(self,*args,**kwargs):
        super(CustomUserCreationForm,self).__init__(*args,**kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['email','name','last_name','profile_image','username']
        def __init__(self,*args,**kwargs):
            super(CustomUserCreationForm,self).__init__(*args,**kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class':'input'})
class EditPasswordForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['password1','password2']
        def __init__(self,*args,**kwargs):
            super(CustomUserCreationForm,self).__init__(*args,**kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class':'input'})
