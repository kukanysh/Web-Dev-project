from django.db import models

# Create your models here.

class ProductManager(models.Manager):
    def get_featured_products(self):
        # Example: Retrieve products with a rating greater than 4.5
        return self.filter(rating__gt=4.5)
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"

    class Meta:
        verbose_name_plural = "categories"


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    brand = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.TextField()
    rating = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    objects = ProductManager()

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"

    class Meta:
        verbose_name_plural = "products"


class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order ID: {self.id}, User: {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.FloatField()

    def __str__(self):
        return f"Order ID: {self.order.id}, Product: {self.product.name}, Quantity: {self.quantity}"


class Cart(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f"Cart ID: {self.id}, User: {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Cart ID: {self.cart.id}, Product: {self.product.name}, Quantity: {self.quantity}"
