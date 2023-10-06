from django.contrib import admin
from .models import CarMake,CarModel


# Register your models here.
# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel 
    extra = 3

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('carName', 'dealerId', 'carType', 'year')
    list_filter = ['dealerId']
    search_fields = ['car_model']
# CarMakeAdmin class with CarMode
# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('name',)
    list_filter = ['name']
    search_fields = ['name', 'description']
# Register models here
admin.site.register(CarMake,CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)