from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from author.models import Profile , ProfileStatus


@receiver(post_save, sender = User)
def create_profile(sender , instance, created , **kwargs):
    #print("created", created)
    if(created):
        Profile.objects.create(user=instance)



@receiver(post_save, sender = User)
def create_status(sender , instance, created , **kwargs):
   # print("created", created)
    if(created):
        qs = Profile.objects.filter(user__username = instance).first()
        ProfileStatus.objects.create(user_profile=qs)      
