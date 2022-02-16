from django import forms
from pybo2.models import Question2, Answer2, Comment2



class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question2  # 사용할 모델
        fields = ['subject', 'content']  # QuestionForm에서 사용할 Question 모델의 속성

        labels = {
            'subject': '제목',
            'content': '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer2
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment2
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }

