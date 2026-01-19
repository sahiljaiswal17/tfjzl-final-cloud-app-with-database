from .models import Submission, Choice, Question

def submit_exam(request, course_id):
    if request.method == 'POST':
        submission = Submission.objects.create(
            user=request.user,
            course_id=course_id
        )

        total_score = 0

        for key, value in request.POST.items():
            if key.startswith('question_'):
                choice = Choice.objects.get(id=value)
                submission.choices.add(choice)

                if choice.is_correct:
                    total_score += choice.question.grade

        submission.score = total_score
        submission.save()

        return redirect('exam_result', course_id=course_id)

def show_exam_result(request, course_id):
    course = Course.objects.get(id=course_id)
    submission = Submission.objects.filter(
        user=request.user,
        course=course
    ).last()

    total_score = submission.score
    possible_score = sum(
        question.grade for question in course.question_set.all()
    )

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
