from django.shortcuts import render
from django.http import HttpResponse  # This class builds the response object that views are expected to return
from django.http import Http404

from .models import Pet

def home(request):
    #query for all of our pets
    pets = Pet.objects.all()
    # The render function will pass the responsibility of rendering html onto the templates, so our view only has to be concerned with making the necessary database queries and passing that data into a template. Using the render function means that our views will need template files in order to work.
    # return HttpResponse('<p>home view</p>')  # http response here is unwieldy for html bodies that are larger than a couple lines of text, so we get rid of this
    return render(request, 'home.html', {'pets':pets})

def pet_detail(request, id):
    try:
        pet = Pet.objects.get(id=id)
    # Because the id that someone provides might not exist, we need this exception and then we need to create a 404 import, above
    except Pet.DoesNotExist:
        raise Http404('Pet not found')
    return render(request, 'pet_detail.html', {'pet':pet})

    # return HttpResponse('<p>pet_detail view with the id {}</p>'.format(id))