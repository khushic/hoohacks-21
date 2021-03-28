from django.shortcuts import render, redirect

from .models import Question, Questioncomment, User
from django.forms.models import model_to_dict


def get_all_questions(request):
    all_questions = list(Question.objects.all().values())
    for i in all_questions:
        i["username"] = User.objects.get(id=i["user_id"]).username
        i["tags"] = i["tags"].split(", ")
    context = {
        'all_questions':all_questions
    }
    return render(request, "forum/all_questions.html", context)

def get_question(request, question_id):
    query = Question.objects.get(questionID = question_id)
    question = model_to_dict(query)
    question["username"] = User.objects.get(id=question["user"]).username
    question["tags"] = question["tags"].split(", ")
    try:
        all_comments = list(Questioncomment.objects.filter(post = question_id).values())
        for i in all_comments:
            i["username"] = User.objects.get(id=i["user_id"]).username
    except Questioncomment.DoesNotExist:
        all_comments = None
    context = {
        'question' : question,
        'all_comments' : all_comments
    }
    return render(request, "forum/question_view.html", context)

def create_question(request):
    if request.method == "POST":
        created_obj = Question.objects.get_or_create(
            title=request.POST.get('question_name'),
            content=request.POST.get('description'),
            tags=request.POST.get('tags'),
            user_id=request.user.id,
        )
    return redirect("../")

def create_comment(request, question_id):
    q = Question.objects.get(questionID = question_id)
    if request.method == "POST":
        created_obj = Questioncomment.objects.get_or_create(
            comment=request.POST.get('comment'),
            user_id=request.user.id,
            post_id=q.questionID,
        )
    query = Question.objects.get(questionID = question_id)
    question = model_to_dict(query)
    question["username"] = User.objects.get(id=question["user"]).username
    question["tags"] = question["tags"].split(", ")
    try:
        all_comments = list(Questioncomment.objects.filter(post = question_id).values())
        for i in all_comments:
            i["username"] = User.objects.get(id=i["user_id"]).username
    except Questioncomment.DoesNotExist:
        all_comments = None
    context = {
        'question' : question,
        'all_comments' : all_comments
    }
    return render(request, "forum/question_view.html", context)
