from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, default = "name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "products"

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models)

    def __str__(self):
        return self.product

    class Meta:
        verbose_name_plural = "orders"
