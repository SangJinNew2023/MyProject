
from django.urls import path

from .views import base_views, question_views, answer_views, comment_views

app_name = 'myboard'

urlpatterns = [
    #base_views.py
    path("", base_views.index, name='index'),
    path("<str:category_name>/", base_views.index, name='index'),
    #question_views.py
    path("question/<int:question_id>/", base_views.detail, name='detail'),
    path("question/create/", question_views.question_create, name='question_create'),
    path("question/modify/<int:question_id>/", question_views.question_modify, name='question_modify'),
    path("question/delete/<int:question_id>/", question_views.question_delete, name='question_delete'),
    path("question/vote/<int:question_id>/", question_views.question_vote, name='question_vote'),
    #answer_views.py
    path("answer/create/<int:question_id>/", answer_views.answer_create, name='answer_create'),
    path("answer/modify/<int:answer_id>/", answer_views.answer_modify, name='answer_modify'),
    path("answer/delete/<int:answer_id>/", answer_views.answer_delete, name='answer_delete'),
    path('answer/vote/<int:answer_id>/', answer_views.answer_vote, name='answer_vote'),
    # comment_views.py
    path("comment/create/answer/<int:answer_id>/", comment_views.comment_create_answer, name='comment_create_answer'),
    path("comment/modify/answer/<int:comment_id>/", comment_views.comment_modify_answer, name='comment_modify_answer'),
    path("comment/delete/answer/<int:comment_id>/", comment_views.comment_delete_answer, name='comment_delete_answer'),


]