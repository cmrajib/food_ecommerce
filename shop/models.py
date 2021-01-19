from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=150)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='product')
    title = models.CharField(max_length=150)
    content = models.TextField()
    longcontent = models.TextField()
    price = models.FloatField(default=0.0)
    discountprice = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0,blank=True)
    hit = models.PositiveIntegerField(default=0)
    image = models.ImageField(blank=True, null=True, upload_to='uploads/')
    shipping = models.CharField(max_length=50, default='1 day shipping. Free pickup')
    Weight = models.CharField(max_length=50)
    DateArrived = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title

