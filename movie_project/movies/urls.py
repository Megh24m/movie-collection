from django.urls import path

from .views import (
    MovieListView,
    MovieDetailView,
    register_view,
    login_view,
    logout_view,
    add_to_favorite,
    remove_favorite,
    wishlist_view,
    remove_selected_favorites,
    clear_wishlist
)

urlpatterns = [

    path(
        "",
        MovieListView.as_view(),
        name="movie_list"
    ),

    path(
        "movie/<int:pk>/",
        MovieDetailView.as_view(),
        name="movie_detail"
    ),

    path(
        "register/",
        register_view,
        name="register"
    ),

    path(
        "login/",
        login_view,
        name="login"
    ),

    path(
        "logout/",
        logout_view,
        name="logout"
    ),

    path(
        "wishlist/",
        wishlist_view,
        name="wishlist"
    ),

    path(
        "favorite/add/<int:movie_id>/",
        add_to_favorite,
        name="add_to_favorite"
    ),

    path(
        "favorite/remove/<int:movie_id>/",
        remove_favorite,
        name="remove_favorite"
    ),

    path(
        "wishlist/remove-selected/",
        remove_selected_favorites,
        name="remove_selected_favorites"
    ),

    path(
        "wishlist/clear/",
        clear_wishlist,
        name="clear_wishlist"
    ),
]