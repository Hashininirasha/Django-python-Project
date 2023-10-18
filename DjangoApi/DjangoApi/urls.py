from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from School.views import SchoolView, ClassView, Assessment_Areas_View, AnswersView, AwardsView, StudentView, SubjectView, CategoryView, SummeryView
from rest_framework import routers

route = routers.DefaultRouter()
route.register("", SchoolView, basename='SchoolView')

route_ClassView = routers.DefaultRouter()
route_ClassView.register("", ClassView, basename='ClassView')

assessment_areas_view = routers.DefaultRouter()
assessment_areas_view.register("", Assessment_Areas_View, basename='Assessment_Areas_View')

route_AnswersView = routers.DefaultRouter()
route_AnswersView.register("", AnswersView, basename='AnswersView')

route_AwardsView = routers.DefaultRouter()
route_AwardsView.register("", AwardsView, basename='AwardsView')  

route_StudentView = routers.DefaultRouter()
route_StudentView.register("", StudentView, basename='StudentView') 

route_SubjectView = routers.DefaultRouter()
route_SubjectView.register("", SubjectView, basename='SubjectView') 

route_CategoryView = routers.DefaultRouter()
route_CategoryView.register("", CategoryView, basename='CategoryView') 


route_SummeryView = routers.DefaultRouter()
route_SummeryView.register("", SummeryView, basename='SummeryView') 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('school/', include(route.urls)),
    path('class/', include(route_ClassView.urls), name='class-view'),
    path('Assessment/', include(assessment_areas_view.urls), name='Assessment_Areas-View'),
    path('Answers/', include(route_AnswersView.urls), name='AnswersView'),
    path('Awards/', include(route_AwardsView.urls), name='AwardsView'), 
    path('Student/', include(route_StudentView.urls), name='StudentView'), 
    path('Subject/', include(route_SubjectView.urls), name='SubjectView'), 
    path('Category/', include(route_CategoryView.urls), name='CategoryView'),
    path('Summery/', include(route_SummeryView.urls), name='SummeryView'),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
