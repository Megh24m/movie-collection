from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import (
    Movie,
    Language,
    Genre,
    Favorite
)


# ==========================
# REGISTER
# ==========================
def register_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get(
            "confirm_password"
        )

        # USERNAME CHECK
        if User.objects.filter(
            username=username
        ).exists():

            messages.error(
                request,
                "Username already exists"
            )

            return redirect("register")

        # PASSWORD CHECK
        if password != confirm_password:

            messages.error(
                request,
                "Passwords do not match"
            )

            return redirect("register")

        # CREATE USER
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # AUTO LOGIN
        login(request, user)

        return redirect("movie_list")

    return render(
        request,
        "register.html"
    )


# ==========================
# LOGIN
# ==========================
def login_view(request):

    if request.method == "POST":

        username = request.POST.get(
            "username"
        )

        password = request.POST.get(
            "password"
        )

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(
                request,
                user
            )

            return redirect(
                "movie_list"
            )

        else:

            messages.error(
                request,
                "Invalid username or password"
            )

    return render(
        request,
        "login.html"
    )


# ==========================
# LOGOUT
# ==========================
def logout_view(request):

    logout(request)

    return redirect("login")


# ==========================
# ADD TO FAVORITE
# ==========================
@login_required
def add_to_favorite(
    request,
    movie_id
):

    movie = get_object_or_404(
        Movie,
        id=movie_id
    )

    Favorite.objects.get_or_create(
        user=request.user,
        movie=movie
    )

    return redirect(
        "movie_detail",
        pk=movie.id
    )


# ==========================
# REMOVE FAVORITE
# ==========================
@login_required
def remove_favorite(
    request,
    movie_id
):

    movie = get_object_or_404(
        Movie,
        id=movie_id
    )

    Favorite.objects.filter(
        user=request.user,
        movie=movie
    ).delete()

    return redirect(
        "movie_detail",
        pk=movie.id
    )


# ==========================
# WISHLIST PAGE
# ==========================
@login_required(login_url="login")
def wishlist_view(request):

    favorites = Favorite.objects.filter(
        user=request.user
    )

    return render(
        request,
        "wishlist.html",
        {
            "favorites": favorites
        }
    )


# ==========================
# REMOVE SELECTED MOVIES
# ==========================
@login_required(login_url="login")
def remove_selected_favorites(
    request
):

    if request.method == "POST":

        movie_ids = request.POST.getlist(
            "selected_movies"
        )

        Favorite.objects.filter(
            user=request.user,
            movie_id__in=movie_ids
        ).delete()

    return redirect(
        "wishlist"
    )


# ==========================
# CLEAR ALL WISHLIST
# ==========================
@login_required(login_url="login")
def clear_wishlist(
    request
):

    Favorite.objects.filter(
        user=request.user
    ).delete()

    return redirect(
        "wishlist"
    )


# ==========================
# MOVIE LIST
# ==========================
class MovieListView(ListView):

    model = Movie
    template_name = "movie_list.html"
    context_object_name = "movies"

    def get_queryset(self):

        queryset = Movie.objects.select_related(
            "language",
            "genre"
        )

        search = self.request.GET.get(
            "search"
        )

        language = self.request.GET.get(
            "language"
        )

        genre = self.request.GET.get(
            "genre"
        )

        filter_type = self.request.GET.get(
            "filter"
        )

        if search:
            queryset = queryset.filter(
                movie_name__icontains=search
            )

        if language:
            queryset = queryset.filter(
                language_id=language
            )

        if genre:
            queryset = queryset.filter(
                genre_id=genre
            )

        if filter_type == "top":
            queryset = queryset.order_by(
                "-rating"
            )

        elif filter_type == "popular":
            queryset = queryset.order_by(
                "-collection"
            )

        elif filter_type == "new":
            queryset = queryset.order_by(
                "-released_year"
            )

        else:
            queryset = queryset.order_by(
                "-created_at"
            )

        return queryset

    def get_context_data(
        self,
        **kwargs
    ):

        context = super().get_context_data(
            **kwargs
        )

        context[
            "languages"
        ] = Language.objects.all()

        context[
            "genres"
        ] = Genre.objects.all()

        context[
            "selected_language"
        ] = self.request.GET.get(
            "language",
            ""
        )

        context[
            "selected_genre"
        ] = self.request.GET.get(
            "genre",
            ""
        )

        context[
            "search"
        ] = self.request.GET.get(
            "search",
            ""
        )

        return context


# ==========================
# MOVIE DETAIL
# ==========================
class MovieDetailView(
    DetailView
):

    model = Movie
    template_name = "movie_detail.html"
    context_object_name = "movie"

    def get_context_data(
        self,
        **kwargs
    ):

        context = super().get_context_data(
            **kwargs
        )

        movie = self.object

        related_movies = Movie.objects.filter(
            genre=movie.genre
        ).exclude(
            id=movie.id
        )[:6]

        context[
            "related_movies"
        ] = related_movies

        # CHECK FAVORITE
        is_favorite = False

        if self.request.user.is_authenticated:

            is_favorite = Favorite.objects.filter(
                user=self.request.user,
                movie=movie
            ).exists()

        context[
            "is_favorite"
        ] = is_favorite

        return context