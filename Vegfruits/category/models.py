from django.db import models

class Category(models.Model):
    categoryname=models.CharField(max_length=20,unique=True)
    cat_image=models.ImageField(upload_to='images')
    slug = models.SlugField(max_length=200, unique=True)
    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'
    def __str__(self):
        return self.categoryname
