from . import views
from django.urls import path
app_name='searchapp'

urlpatterns=[
        path('new/',views.SearchResult,name='SearchResult'),
]