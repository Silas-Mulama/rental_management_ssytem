from django.urls import path
from schools import views
urlpatterns = [
   path('',views.Home,name='all_sch'),
   path('schools/add/',views.add_school,name='add_sch'),
   path('schools/<str:pk>/',views.apartment,name='apart')
]
