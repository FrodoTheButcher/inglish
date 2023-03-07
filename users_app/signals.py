

##ca sa functioneze,trebuie adaugate la apps.py
from django.db.models.signals import post_delete,post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

#@receiver(post_save,sender=Profile)
def createProfile(sender, instance, created,**kwargs):
    if created:##in caz ca e prima data cand este creat
        user = instance##instance reprezinta senderul
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
            last_name=user.last_name
        )
       


#@receiver(post_delete,sender=Profile)
def deleteUser(sender,instance,**kwargs):
    user = instance.user##userul din profile
    user.delete()

##mereu cand creezi un user se apeleaza functia
post_save.connect(createProfile,sender=User)


##mereu cand un profil e sters,se sterge userul
post_delete.connect(deleteUser,sender=Profile)