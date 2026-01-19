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
