from django.urls import path
from .views import StudentView



app_name = "students"
# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('students/', StudentView.as_view()),
    path('student/<int:pk>', StudentView.as_view()),

]