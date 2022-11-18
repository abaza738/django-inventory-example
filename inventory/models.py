from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=120)
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField()
    ingredients = models.ManyToManyField(
        to=Ingredient, through='ProductIngredients')

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    products = models.ManyToManyField(to=Product, through='OrderProducts')

    @property
    def total(self):
        return self.products.aggregate(models.Sum('price'))


# Join Classes for Many-To-Many Relationships


class ProductIngredients(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()


class OrderProducts(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
