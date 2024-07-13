from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User,Group
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta
from django.shortcuts  import get_object_or_404


def validate_no_numbers(value):
    if any(char.isdigit() for char in value):
        raise ValidationError("This field should not contain numbers.")

class Shop(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name='shop')
    shopName = models.CharField(max_length=200)
    adress=models.CharField(max_length=200,default='bahirdar',validators=[validate_no_numbers])
    registration_date=models.DateField(auto_now_add=True)
    valid_from=models.DateTimeField(blank=True,null=True)
    valid_to=models.DateTimeField(blank=True,null=True)
    is_active=models.BooleanField(default=False)

    def activate_shop(self,duration):
        self.valid_from=timezone.now()
        self.valid_to=self.valid_from + duration
        self.is_active=True
        self.save()
        user=get_object_or_404(User,username=self.owner.username)
        user.is_staff=True
        user.save()
       

        group, created = Group.objects.get_or_create(name='shoponwer')
        if not created:
            self.owner.groups.add(group)
        else:
            self.owner.groups.add(created)


    def deactivate_shop(self):
        self.is_active=False
        self.save()  


    

        
    


    def __str__(self):
        return self.shopName
class Category(models.Model):
    shop = models.ForeignKey(Shop, related_name='categories', on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,unique=True) #t o build beautiful URLs
    has_sub_catagory=models.BooleanField(default=False)
    class Meta:
        ordering=['name']
        indexes=[models.Index(fields=['name']),]
        verbose_name='category'# specifies the human-readable singular name for the model.
        verbose_name_plural='categories'
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])
class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    class Meta:
        ordering=['name']
        indexes=[models.Index(fields=['name']),]
        verbose_name='subcategory'# specifies the human-readable singular name for the model.
        verbose_name_plural='subcategories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        
        return reverse('shop:product_list_by_subcategory', args=[self.slug])    

class Product(models.Model):
    category=models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, related_name='products', null=True, blank=True, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, related_name='products', on_delete=models.CASCADE,null=True,blank=True)
    
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200)
    image=models.ImageField(upload_to='products/%y/%m/%d',blank=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
     
    class Meta:
        ordering=['name']
        indexes=[models.Index(fields=['id','slug']),
                 models.Index(fields=['name']),
                 models.Index(fields=['-created']),]
        
    def __str__(self):
        return self.name  
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
 

       

class ShopSubscrioptionPlan(models.Model):
    PLAN_CHOICE=[
        ('monthly','Monthly'),
        ('six_months','Six Months'),
        ('yearly','Yearly'),
    ]
    plan_name=models.CharField(max_length=20,choices=PLAN_CHOICE)
    price=models.DecimalField(max_digits=10,decimal_places=2)
        
    def __str__(self):
        return self.plan_name  
    
class ProductRecommandation(models.Model):
    product_id=models.IntegerField()  
    purchased_with_product_id=models.IntegerField()  
    purchased_with_times=models.IntegerField(default=1)

    def __str__(self):
        return str(self.product_id)
