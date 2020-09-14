from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from .utils import get_random_code
# Create your models here.

# Install pillow
#PROFILE_MODEL
class Profile(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    age = models.IntegerField(default=22)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="Tell us more",max_length=200)
    email = models.EmailField(max_length=200, blank=True)
    country = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(default='ava.png', upload_to='avatars/')
    friends = models.ManyToManyField(User, blank=True, related_name='friends')
    slug = models.SlugField(unique=True, blank=True) #optional part
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}-{self.created.strftime('%d-%h-%y')}" # F is a new format to represent the string
    
    def save(self, *args, **kwargs): #https://www.programiz.com/python-programming/args-and-kwargs
        x = False #optional part
        if self.first_name and self.last_name:
            to_slug = slugify(str(self.first_name) + " " + str(self.last_name))
            x = Profile.objects.filter(slug=to_slug).exists()
            while x:
                to_slug = slugify(to_slug + " " + str(get_random_code()))
                x = Profile.objects.filter(slug=to_slug).exists()
        else:
            to_slug = str(self.user)
        self.slug = to_slug
        super().save(*args, **kwargs)  

STATUS_CHOICES = (  #Tuple part for choice
    ('send','send'),      #(for db , for user view )
    ('accept','accept'),
    ('reject', 'reject')
)                  

#RELEATIONSHIP_MODEL
class Releationship(models.Model): 
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=6, choices=STATUS_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}" # F is a new format to represent the string
    



