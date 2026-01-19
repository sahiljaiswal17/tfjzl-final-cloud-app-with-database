from django.shortcuts import render, redirect
from .models import Course, Question, Choice, Submission


def course_details(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(
        request,
        'onlinecourse/course_details_bootstrap.html',
        {'course': course}
    )


def submit_exam(request, course_id):
    course = Course.objects.get(id=course_id)
    submission = Submission.objects.create(
        user=request.user,
        course=course
    )

    for key, value in request.POST.items():
        if key.startswith('question_'):
            choice = Choice.objects.get(id=value)
            submission.choices.add(choice)

    submission.save()

    return redirect(
        'show_exam_result',
        course_id=course.id,
        submission_id=submission.id
    )


def show_exam_result(request, course_id, submission_id):
    course = Course.objects.get(id=course_id)
    submission = Submission.objects.get(id=submission_id)

    total_score = 0
    possible_score = 0

    for question in course.question_set.all():
        possible_score += question.grade
        if question.is_get_score(submission):
            total_score += question.grade

    return render(
        request,
        'onlinecourse/exam_result_bootstrap.html',
        {
            'course': course,
            'submission': submission,
            'total_score': total_score,
            'possible_score': possible_score,
        }
    )
