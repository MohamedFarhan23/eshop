from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.signals import post_save

# Creating a profile for each users
class Profile(models.Model):
    user  = models.OneToOneField(User,on_delete=models.CASCADE,blank=True)
    user_image = models.ImageField(default='delhi.jpg',null=True,blank=True)
    first_name = models.CharField(max_length=50,blank=True)
    last_name = models.CharField(max_length=50,blank=True)
    gender  = models.CharField(max_length=20,null=True)
    address = models.TextField(blank=True)
    # phone number using regularexpression
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    
    def __str__(self):
        return str(self.user)
# reciver signal
def profile_created(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('profile created')
# signal connecting the receiver and user
post_save.connect(profile_created,sender=User)

# category class contains only name of categoris and relation with product class
class Category(models.Model):
    title = models.CharField(max_length=35)
    cat_image = models.ImageField(null=True,blank=True)
    rate = models.FloatField(null=True)

    def __str__(self):
        return self.title

# product class relation with category
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    pro_image = models.ImageField(null=True,blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=350)
    price = models.FloatField()

    def __str__(self):
        return self.title

# creating a add to cart system
class Addcart(models.Model):
    buyer = models.ForeignKey(User,on_delete=models.CASCADE)
    cart_image = models.ImageField(null=True,blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=350)
    price = models.FloatField()

    def __str__(self):
        return self.title

class Buy(models.Model):
    buyer = models.ForeignKey(User,on_delete=models.CASCADE)
    order_image = models.ImageField(null=True,blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=350)
    price = models.FloatField()

    def __str__(self):
        return self.title



