from django.urls import path
from .views import *
urlpatterns =[
    path('',index,name='index'),
    path('h404',h404,name='h404' ),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('courses/', courses, name="courses"),
    path('team/', team, name="team"),
    path('testimonial/', testimonial, name="testimonial")
]
