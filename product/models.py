from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=130, unique=True)
    description = models.TextField(blank=True)
    
    class Meta():
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_image/', blank=True)
    
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category}'
    
    

class Basket(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product = models.ForeignKey('Products', on_delete=models.CASCADE)
    created =models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=0)
    
    def __str__(self) -> str:
        return f'Корзина для {self.user.username} | Продукт: {self.product.name}'

    