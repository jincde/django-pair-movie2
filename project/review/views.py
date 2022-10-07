from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import MovieInfo, Review


def index(request):
    reviews = Review.objects.order_by("-pk")
    Review_len = len([*Review.objects.all()])
    context = {
        "reviews": reviews,
        "Review_len": Review_len,
    }

    return render(request, "review/index.html", context)


def main(request):
    movie_info = MovieInfo.objects.all()
    Review_len = len([*Review.objects.all()])
    context = {
        "movie_info": movie_info,
        "Review_len": Review_len,
    }
    return render(request, "review/main.html", context)


def create(request, pk):
    Review_len = len([*Review.objects.all()])
    movie_info = MovieInfo.objects.get(pk=pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        grade = int(request.POST.get("review_grade"))
        if review_form.is_valid():
            review_form.save()
            review = Review.objects.order_by("-pk")[0]
            # 처음에 movie_title = movie_info.movie_name 으로 했다가 pk 로 하는게 나을거같아서 pk 로 바꿈
            review.movie_pk = movie_info.pk
            review.save()
            movie_info.movie_grade += grade
            movie_info.vote += 1
            movie_info.avg_grade = movie_info.movie_grade / movie_info.vote
            movie_info.save()
            return redirect("review:index")

    else:
        review_form = ReviewForm()

    context = {
        "review_form": review_form,
        "movie_title": movie_info.movie_name,
        "Review_len": Review_len,
    }

    return render(request, "review/create.html", context)


def detail(request, pk):
    Review_len = len([*Review.objects.all()])
    review = Review.objects.get(pk=pk)

    context = {
        "review": review,
        "Review_len": Review_len,
    }

    return render(request, "review/detail.html", context)


def update(request, pk):
    Review_len = len([*Review.objects.all()])
    review = Review.objects.get(pk=pk)
    old_grade = review.review_grade
    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=review)

        if review_form.is_valid():
            review_form.save()
            review = Review.objects.get(pk=pk)
            new_grade = review.review_grade
            if old_grade != new_grade:
                movie_pk = review.movie_pk
                movie_info = MovieInfo.objects.get(pk=movie_pk)
                movie_info.movie_grade -= old_grade
                movie_info.movie_grade += new_grade
                movie_info.avg_grade = movie_info.movie_grade / movie_info.vote
                movie_info.save()
            else:
                pass

            return redirect("review:detail", review.pk)

    else:
        review_form = ReviewForm(instance=review)

    context = {
        "review": review,
        "review_form": review_form,
        "Review_len": Review_len,
    }

    return render(request, "review/update.html", context)


def delete(request, pk):
    review = Review.objects.get(pk=pk)
    grade = review.review_grade
    movie_pk = review.movie_pk
    # 처음에 movie_title 로 했다가 pk 로 하는게 나을거같아서 pk 로 바꿈
    movie_info = MovieInfo.objects.get(pk=movie_pk)
    movie_info.movie_grade -= grade
    movie_info.vote -= 1
    if movie_info.vote:
        movie_info.avg_grade = movie_info.movie_grade / movie_info.vote
    else:
        movie_info.avg_grade = 0
    movie_info.save()
    review.delete()

    return redirect("review:index")


def search_review(request):
    review_title = request.GET.get("review-title")
    Review_len = len([*Review.objects.all()])
    retrieved_review_data = Review.objects.filter(title__icontains=review_title)
    context = {
        "retrieved_review_data": retrieved_review_data,
        "Review_len": Review_len,
    }

    return render(request, "review/index.html", context)
