from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Question


def submit(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    questions = Question.objects.all()
    score = 0
    total = questions.count()
    results = []

    for question in questions:
        selected_answer = request.POST.get(f"question_{question.id}")

        correct_choice = question.choice_set.filter(is_correct=True).first()

        is_correct = (
            correct_choice is not None
            and selected_answer == str(correct_choice.id)
        )

        if is_correct:
            score += 1

        results.append({
            "question": question,
            "selected_answer": selected_answer,
            "correct_answer": correct_choice,
            "is_correct": is_correct,
        })

    request.session["score"] = score
    request.session["total"] = total

    return render(
        request,
        "OnlineCourse/exam_result.html",
        {
            "course": course,
            "score": score,
            "total": total,
            "results": results,
        },
    )


def show_exam_result(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    score = request.session.get("score", 0)
    total = request.session.get("total", 0)

    questions = Question.objects.all()
    results = []

    for question in questions:
        correct_choice = question.choice_set.filter(is_correct=True).first()

        results.append({
            "question": question,
            "correct_answer": correct_choice,
        })

    return render(
        request,
        "OnlineCourse/exam_result.html",
        {
            "course": course,
            "score": score,
            "total": total,
            "results": results,
        },
    )
