from django.shortcuts import render, redirect, reverse
from .models import Question, Customers, Answers
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
import uuid, random

# Create your views here.


def home(request):
    return render(request, "survey/index.html", context={})


@csrf_exempt
def handler(request, cust_id, id):
    MIN_Q_ID = 1
    # Find out question
    ques_list = [
        question for question in Question.objects.all()
    ]  # will call the database only one time
    n_questions = max(MIN_Q_ID, len(ques_list))  # [0, n]
    if n_questions <= 0:
        raise Http404("Please insert questions for survey")
    print(id, [q.id for q in ques_list])
    current_question = [q for q in ques_list if q.id == id]
    assert len(current_question) == 1
    current_question = current_question[0]
    is_last = current_question.id == ques_list[-1].id
    # Question has been saved
    if request.method == "POST":
        # save the answer to database
        answer = request.POST["ans"]
        print(answer)
        c = Customers.objects.get(cust_id=cust_id)
        resp = Answers(customer=c, ques=current_question, text=answer)
        resp.save()
        # --- show next question
        action = request.POST["action"]
        new_id = id
        if action == "previous":
            new_id = max(MIN_Q_ID, id - 1)
        elif action == "next":
            new_id = min(n_questions, id + 1)
        elif action == "submit":
            return redirect("/close")
        return redirect(f"/questions/{cust_id}/{new_id}")
    return render(
        request,
        "survey/form.html",
        context={
            "question": current_question,
            "cust_id": cust_id,
            "islast": is_last,
        },
    )


@csrf_exempt
def start(request):
    cust_id = int(random.random() * 100_000)
    c = Customers(cust_id=cust_id)
    c.save()
    return redirect(f"questions/{cust_id}/1")


def close(request):
    return render(request, "survey/close.html")
