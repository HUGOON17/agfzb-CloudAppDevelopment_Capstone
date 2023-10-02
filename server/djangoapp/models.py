from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default="Toyota")
    description = models.CharField(max_length=150)
    def __str__(self):
        return "name: " + self.name + " Description: " + self.description


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

class CarModel(models.Model):
    maker = models.ForeignKey(CarMake, null=False, on_delete=models.CASCADE)
    dealerId = models.IntegerField(null=False)
    carName = models.CharField(null=False, max_length=30, default="Corolla")
    carType = models.CharField(null=False, max_length=30, default="Sedan")
    year = models.IntegerField(default=2023)
    def __str__(self):
        return "Car: " + self.carName + " " + str(self.year)


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:

    def __init__(self, dealership=None, name=None, purchase=None, review=None, purchase_date=None, car_make=None, car_model=None, car_year=None, sentiment=None, id=None):
        if dealership is not None:
            self.dealership = dealership
        if name is not None:    
            self.name = name
        if purchase is not None:    
            self.purchase = purchase
        if review is not None:
            self.review = review
        if purchase_date is not None:
            self.purchase_date = purchase_date
        if car_make is not None:
            self.car_make = car_make
        if car_model is not None:
            self.car_model = car_model
        if car_year is not None:
            self.car_year = car_year
        self.sentiment = sentiment
        if id is not None:
            self.id = id

    def __str__(self):
        return "Name: " + self.name + ' ' + self.car_make + ' ' + self.car_model + ' ' + self.car_year  + '  Review: ' + self.review
