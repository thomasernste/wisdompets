from django.db import models

#model for tracking each pet - the (model.Model) argument is what makes it a model
class Pet(models.Model):
    # Each sex choice is a tuple, where first value is stored in database, and second is used for display in forms and in the django admin
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    #max_length can be shorter for these below because they will never be really long
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True) #blank=True attribute is offered here as possible because the breed might be unknown or there may be no breed
    description = models.TextField() #Since description length is unknown and may be long, text field is used to allow a no length limits field
    #max_length for sex indicates that only one gender/sex is used
    #blank=True is used because some pets may not be identifiable by sex
    sex = models.CharField(choices=SEX_CHOICES, max_length=1, blank=True) #choices attribute used because you want to limit the options
    submission_date = models.DateTimeField()
    #null=True is in case pets are rescued with unknown age
    #null=True is better than blank=True for this attribute because blank=True results in zero, and that would be misleading because it would seem like we're saying the pet is less than 1 year old
    age = models.IntegerField(null=True)
    # need to define relationship between the Pet and Vaccine models since a pet can have many vaccines and the same vaccine can be applied to many pets. This is a ManyToMany relationship so we'll use the ManyToMany field. We can put this
    #this attribute is required to link this model to the Vaccine model. This type of field is unique in that it can be placed either within the Pet or the Vaccine model, and we choose to put it under the Pet model here.
    #Requires a first argument as a string -- the name of the model that it's related to
    #blank=True because some pets may have had no vaccinations, so we don't want this field required
    vaccinations = models.ManyToManyField('Vaccine', blank=True)

#model for tracking vaccines for the pets -- if they have had one, this model would track those vaccinations
class Vaccine(models.Model):
    #this is the name of the vaccine, which is all we need for this model
    name = models.CharField(max_length=50)
    #This method overrides the default method to make it possible to display the vaccinations for the given pet
    def __str__(self):
        return self.name