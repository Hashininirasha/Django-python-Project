
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# from Modules.views import ModulesView
# from Students.views import StudentsView

from rest_framework import routers
# from schools.view import schoolsView

from rest_framework.routers import DefaultRouter



# schools_router = DefaultRouter()
# schools_router.register("", schoolsView, basename='schoolsView')

# Define the urlpatterns to include the router's URLs
urlpatterns = [
    # path('modules/', include(modules_router.urls)),  # Include URLs for ModulesView under 'modules/'
    # path('students/', include(students_router.urls)),  # Include URLs for StudentsView under 'students/'
    # path('school/', include(schools_router.urls)),
]
