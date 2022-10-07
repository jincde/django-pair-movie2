from django import forms
from .models import Review, MovieInfo


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        exclude = (
            "vote",
            "grade",
            "avg_score",
        )
