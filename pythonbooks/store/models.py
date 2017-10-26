from django.db import models
 
#Book title
#Author
#Category
#Cover
#Price
#Description
#ISBN

 
 
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
 
    class Meta:
        ordering  = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
 
    def __str__(self):
        return self.name
 
class Book(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    category = models.ForeignKey(Category, null=True, db_index=True)
    slug = models.SlugField(max_length=200, db_index = True, unique=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    item_id = models.IntegerField(default=0, blank=False)
    isbn = models.IntegerField(blank=True, null=True)
    image = models.URLField(blank=True)
    price = models.IntegerField(blank=True, null=True)

 
 
    class Meta:
        ordering = ('title',)
        verbose_name = 'book'
        verbose_name_plural = 'books'
 
    def __str__(self):
        return self.title

class Price(models.Model):

    value = models.FloatField(blank=True, null=True)
    currency = models.CharField(max_length=3)
    #book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)


    class Meta:
        ordering = ('value',)
        verbose_name = 'Price'
        verbose_name_plural = 'Prices'

    def __str__(self):
        return self.value





