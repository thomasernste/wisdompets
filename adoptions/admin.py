from django.contrib import admin

from .models import Pet

#register the class with the admin to tell it which model its associated. To do this, we use the decorator from the admin model called register. The decorator takes a model class as an argument, so we pass it the Pet model.
@admin.register(Pet)
#The argument in the line below makes the PetAdmin class inherit from admin.ModelAdmin
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'breed', 'age', 'sex']