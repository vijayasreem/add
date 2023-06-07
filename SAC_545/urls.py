# urls.py
from django.urls import path
from .views import view_user_stories, view_user_story_details

urlpatterns = [
    path('stories/', view_user_stories, name='user_stories'),
    path('stories/<int:id>/', view_user_story_details, name='user_story_details'),
]