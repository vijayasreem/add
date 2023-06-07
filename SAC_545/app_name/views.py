# views.py
from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def view_user_stories(request):
    # fetch the user stories from the Jira API
    url = '<URL of Jira API>'
    response = requests.get(url)
    stories = response.json()

    # render the user stories in the front-end application
    context = {
        'stories': stories
    }
    return render(request, 'user_stories.html', context)

def view_user_story_details(request, id):
    # fetch the user story details from the Jira API
    url = '<URL of Jira API>'
    response = requests.get(url)
    stories = response.json()

    # render the user story details in the front-end application
    for story in stories:
        if story['id'] == id:
            context = {
                'story': story
            }
            return render(request, 'user_story_details.html', context)

    # return an error if the user story cannot be found
    return HttpResponse('Error: User story not found.')