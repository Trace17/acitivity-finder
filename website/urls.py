from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.index, name = 'index'),
    path('how_to', views.how_to, name = 'how_to'),
    path('filters_page', views.filters_page, name = 'filters_page'),
]

urlpatterns += staticfiles_urlpatterns()