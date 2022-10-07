from django import forms
from .models import Review
from django.forms import ModelForm, TextInput, EmailInput, NumberInput


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        exclude = ("movie_pk",)
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "리뷰 제목은 30자 이내로 입력해주세요.",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "placeholder": "",
                }
            ),
            "writer": forms.TextInput(
                attrs={
                    "placeholder": "",
                }
            ),
        }
        labels = {
            "title": "리뷰 제목",
            "content": "내용",
            "writer": "작성자",
            "review_grade": "평점",
        }
