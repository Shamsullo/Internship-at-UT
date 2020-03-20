
from django.db import models
from django.db.models import Sum
from django.conf import settings

# Create your models here.

COLOR_CHOICES = (
    ('1', 'Red'),
    ('2', 'Green'),
    ('3', 'Blue')
)


SIZE_CHOICES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large')
)


class Category(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=60)
    superCat = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=False, null=False, default=1)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    color = models.CharField(choices=COLOR_CHOICES, max_length=10)
    size = models.CharField(choices=SIZE_CHOICES, max_length=5)
    price = models.FloatField()
    category = models.ForeignKey(Category, related_name='item_category', blank=True,
                                 null=True, on_delete=models.CASCADE)

    if category:
        sub_cat = models.ForeignKey(SubCategory, related_name='item_sub_cat', blank=True,
                                    null=True, on_delete=models.CASCADE)

    in_cart = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def add_to_cart(self):
        self.in_cart = True

    def remove_from_the_cart(self):
        self.in_cart = False


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_quantity = models.IntegerField()
    delivery_type = models.CharField(max_length=100)
    total_price_of_an_item = models.FloatField()

    # def get_total_price_of_an_item (self):
    #     total_price = self.item.price * self.item_quantity
    #     return total_price

    # item_set.

    # def get_total_price (self):
    #     return self.objects.aggregate(Sum('total_price'))

    # def __str__

# class Order(models.Model):
#     item = models.ForeignKey(Cart, on_delete=models.CASCADE)
