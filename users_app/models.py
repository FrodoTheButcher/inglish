from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import uuid
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    exercises = models.ManyToManyField('Exercise',blank=True)
    name = models.CharField(max_length=200,blank=True,null=True)
    last_name = models.CharField(max_length=200,blank=True,null=True)
    username = models.CharField(max_length=200,blank=True,null=True)
    email = models.EmailField(max_length=500, blank=True,null=True)
    short_intro = models.CharField(max_length=200,blank=True,null=True)
    bio  = models.TextField(blank=True,null=True)
    profile_image = models.ImageField(null=True,blank=True ,upload_to='profiles/',default='profiles/default_profile.png' )
    social_github = models.CharField(max_length=200,blank=True,null=True)
    social_twitter = models.CharField(max_length=200,blank=True,null=True)
    social_linkedin = models.CharField(max_length=200,blank=True,null=True)
    social_youtube = models.CharField(max_length=200,blank=True,null=True)
    social_website = models.CharField(max_length=200,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    
    def __str__(self):
        return str(self.username)




class skill(models.Model):
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200 , blank=True, null=True)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.name)

class todo(models.Model):
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200 , blank=True, null=True)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.name)

class Exercise(models.Model):
    level=models.CharField(default='Beginners',max_length=10,blank=True)
    owner = models.ManyToManyField(Profile,blank=True)
    Name=models.CharField(default="NONE",max_length=50)
    description=models.TextField(default="NONE",max_length=1000)
    dificulty = models.CharField(max_length=10)
    category=models.CharField(max_length=20)
    number=models.IntegerField()
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    Default=models.TextField(max_length=500,default="None")
    Exemple1=models.TextField(max_length=500,default="None")
    Exemple2=models.TextField(max_length=500,default="None")
    tag_name = models.CharField(max_length=10,default="None")
    Answer1default=models.TextField(max_length=200,default="NONE")
    Answer2default=models.TextField(max_length=200,default="NONE")
    Help=models.TextField(max_length=500,default='NONE')
    Code=models.TextField(max_length=5000,default="NONE")
    Image = models.ImageField(null=True,blank=True ,upload_to='ex_easy/',default='profiles/default_profile.png' )
    def __str__(self):
        return str(self.Name)
    
   
    
