path('course/<int:course_id>/submit/', views.submit_exam, name='submit_exam'),
path('course/<int:course_id>/result/', views.exam_result, name='exam_result'),
