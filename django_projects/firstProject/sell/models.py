from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models import Q, Max, Min, QuerySet
from django.core.validators import MaxValueValidator, MinValueValidator
from sell.account.models import Profile




from sell.account.models import Profile
# Create your models here.
# module
# models


class Store(models.Model):
    owner = models.OneToOneField(Profile, on_delete =models.CASCADE)
    tagline = models.CharField(max_length=200)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
    @admin.display(description= "show total products")
    def total_products(self):
        total = self.products.count()
        return total

class Category(models.Model):
    #owner
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return super().__str__()

class Products(models.Model):
    store = models.ForeignKey(Store,on_delete=models.DO_NOTHING, related_name='products', null=True)
    #owner
    Category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name= "products", null=True)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=10)
    is_available = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)
    rating = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name}, {self.desc}"

    def discount(self, discount = 20):
        self.price = self.price * (discount/ 100)
        return self.price

    def __str__(self) -> str:
        return super().__str__()
    
    @property
    def num_reviews(self):
        num = self.ratings.count()

    @num_reviews.getter
    def get_num_reviews(self):
        return self.num_reviews
    
    def average_rating(self):
        rating = self.ratings.aggregate(models.Sum('rating'))
        total = rating.get('ratings_sum')
        # print(rating)
        return total/ self.get_num_reviews
    

    class Meta:
        ordering = ('name' , '-price',)
        verbose_name = "Products"
        

class Rating(models.Model):
    product = models.ForeignKey(Products, related_name= 'ratings' ,on_delete=models.CASCADE)
    rating = models.IntegerField(default=(0), validators=[MaxValueValidator(5), MinValueValidator(0)])
    remark = models.CharField(max_length=200)


    def __str__(self) -> str:
        return f"{self.rating}"