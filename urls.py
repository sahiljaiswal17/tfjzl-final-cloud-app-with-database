
from django.urls import path
from . import views

urlpatterns = [
    path('course/<int:course_id>/submit/', views.submit_exam, name='submit_exam'),
    path('course/<int:course_id>/result/', views.show_exam_result, name='show_exam_result'),
]
