from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
import time
from .web_scrape import get_random_result
from .web_scrape import get_return_activity
from .web_scrape import get_link_to_result
from .web_scrape import get_image_of_result
from .format_activity import format_activity


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def how_to(request):
    return render(request, 'how_to.html', {})

def filters_page(request):
    if request.method == "POST":
        return HttpResponseRedirect('activity_page/')
    return render(request, 'filters_page.html', {})

def activity_page(request):
    category = request.POST['category']
    city = request.POST['city']
    state = request.POST['state']
    specifics = request.POST['specifics']
    url = format_activity(category,city,state,specifics)
    print(url)
    random_result = get_random_result(url)
    return_activity = get_return_activity(random_result)
    link = get_link_to_result(random_result)
    random_activity = prettify_result(return_activity)
    image = get_image_of_result(link)
    context = {'random_activity': random_activity, 'category': category, 'city': city, 'state': state, 'specifics': specifics, 'link': link, 'image': image}
    return render(request, 'activity_page.html', context) 


def prettify_result(activity):
    counter = 0
    current_char = activity[counter]
    new_string = ""
    while current_char != ".":
        counter += 1
        current_char = activity[counter]
    counter += 1
    counter += 1
    while counter < len(activity):
        new_string += activity[counter]
        counter += 1
    return new_string

