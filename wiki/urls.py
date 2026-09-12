from django.urls import path
from . import views


urlpatterns = [
    path('', views.WikiList.as_view(), name='wiki_list'),
]