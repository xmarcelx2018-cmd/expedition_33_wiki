from django.urls import path
from . import views

urlpatterns = [
    path('characters/', views.WikiList.as_view(category='character'), name='characters'),
    path('weapons/', views.WikiList.as_view(category='weapon'), name='weapons'),
    path('locations/', views.WikiList.as_view(category='location'), name='locations'),
]