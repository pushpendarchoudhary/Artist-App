# artist/urls.py

from django.urls import path
from .views import ArtistListView
from .import views
urlpatterns = [
    path('', views.home, name="home"),
    path('api/register', views.signup, name="signup"),
    path('api/signin', views.signin, name="signin"),
    path('api/signout', views.signout, name="signout"),
    path('api/works', views.Work_list_view, name='work-list'),
    path('api/artists/', ArtistListView.as_view(), name='artist-list'),

]
