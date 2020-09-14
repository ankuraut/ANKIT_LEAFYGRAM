#This file gonna use signal to create profile automatic when a user create a new profile.
from django.db.models.signals import post_save #used to send information at end of the signal
from django.contrib.auth.models import User #user model
from django.dispatch import receiver  #for register signals (decorator)
from .models import Profile , Releationship #profile model

@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs): #....., instance of a user , boolean value
    #print('sender', sender)
    #print('instance', instance)
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=Releationship)
def post_save_add_friends(sender, instance, created, **kwargs): #....., instance of a user , boolean value
    sender_ = instance.sender #new variable = old model
    receiver_ = instance.receiver
    if instance.status == 'accept':
        sender_.friends.add(receiver_.user)
        receiver_.friends.add(sender_.user)
        sender_.save()
        receiver_.save()

