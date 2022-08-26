from django.urls import path
from .views import home
# from .views import CitiesList
urlpatterns = [
    # path('', CitiesList.as_view(), name="home")

    path('',home,name="home")
]