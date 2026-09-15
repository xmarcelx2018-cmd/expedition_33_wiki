from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('characters/', views.WikiList.as_view(category='character'), name='characters'),
    path('weapons/', views.WikiList.as_view(category='weapon'), name='weapons'),
    path('locations/', views.WikiList.as_view(category='location'), name='locations'),
    path('create/', views.WikiCreate.as_view(), name='wiki_create'),
    path('my-entries/', views.MyEntries.as_view(), name='my_entries'),
    path('<int:pk>/edit/', views.WikiUpdate.as_view(), name='wiki_edit'),
    path('<int:pk>/delete/', views.WikiDelete.as_view(), name='wiki_delete'),
    path('<int:pk>/', views.WikiDetail.as_view(), name='wiki_detail'),
]