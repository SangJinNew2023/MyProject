from ..forms import CommentForm
from ..models import Question, Answer, Comment
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='login')
def comment_create_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.answer = answer
            comment.save()
            return redirect('myboard:detail', question_id = comment.answer.question.id)
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'myboard/comment_form.html', context)

@login_required(login_url='login')
def comment_modify_answer(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, "You do not have permission to modify.")
        return redirect('myboard:detail', question_id=comment.answer.question.id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment) #instance 변경될 대상 model 지정
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('myboard:detail', question_id=comment.answer.question.id)
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'myboard/comment_form.html', context)

@login_required(login_url='login')
def comment_delete_answer(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '"You do not have permission to delete."')
        return redirect('myboard:detail', question_id=comment.answer.qeustion.id)
    else:
        comment.delete()
    return redirect('myboard:detail', question_id=comment.answer.question.id)