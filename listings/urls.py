from django.urls import path

from . import views

""""
    one possible solution for pretty urls here: https://wellfire.co/learn/fast-and-beautiful-urls-with-django/
    """
urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    # path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search')
]
