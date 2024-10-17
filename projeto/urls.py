from . import views
from django.urls import path
  
urlpatterns = [
    path('', views.index),
    path('videos/', views.videos_view, name='videos'),
    path('forum/', views.forum_view, name='forum'),
    path('pais_profs/', views.pais_profs_view, name='pais_profs'),

]
