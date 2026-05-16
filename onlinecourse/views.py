from django.shortcuts import render
from django.http import HttpResponse


def submit(request, course_id):
    return HttpResponse("Exam submitted successfully")


def show_exam_result(request, course_id):
    context = {
        'score': 85,
        'total': 100,
        'result': 'Congratulations! You passed the exam.'
    }

    return render(request, 'onlinecourse/exam_result.html', context)
