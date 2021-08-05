from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Category(models.Model):
    
    NAME_MAX_LENGTH = 128
    DESCRIPTION_MAX_LENGTH = 500
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    #Bingo watch attributes
    type = models.CharField(max_length=30,default='') #type of watch
    description = models.CharField(max_length=DESCRIPTION_MAX_LENGTH ,default='') #watch description
    recommend_buy = models.IntegerField(default=0) #recommended buy index
    url = models.URLField(blank=True) #watch vendor link
    picture = models.ImageField(upload_to='product_images', blank=True) #product image

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Page(models.Model):

    NAME_MAX_LENGTH = 128
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    #Bingo watch attributes
    description = models.CharField(max_length=500,default='')

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    
    #Bingo watch attributes
    background = models.CharField(max_length=500,default='')

    def __str__(self):
        return self.user.username

#Bingo watch object
#User comment
class Comment(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    content = models.CharField(max_length=500) #comment content
    rating = models.IntegerField(default=0) #rating
    log_datetime = models.DateTimeField(auto_now=True) #date time

    def __str__(self):
        return self.content[0:10]