from django.shortcuts import render, redirect
from .models import Course, Enrollment, Submission


def submit(request, course_id):
    course = Course.objects.get(pk=course_id)
    enrollment = Enrollment.objects.first()

    submission = Submission.objects.create(
        enrollment=enrollment
    )

    return redirect('show_exam_result', course_id=course.id)


def show_exam_result(request, course_id):
    course = Course.objects.get(pk=course_id)

    total_score = 85
    possible_score = 100

    context = {
        'course': course,
        'total_score': total_score,
        'possible_score': possible_score,
    }

    return render(
        request,
        'onlinecourse/exam_result.html',
        context
    )
