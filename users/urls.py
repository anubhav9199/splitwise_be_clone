from django.urls import path

from users.views import (
    UserSignInView,
    UserSignUpView,
    UpdateUserView,
    GetUserDetailsView,
    UserLogoutView
)

urlpatterns = [
    path(
        "v1/users/signin",
        UserSignInView.as_view(),
        name="user_sign_in",
    ),
    path(
        "v1/users/logout",
        UserLogoutView.as_view(),
        name="user_sign_in",
    ),
    path(
        "v1/users/signup",
        UserSignUpView.as_view(),
        name="user_sign_up",
    ),
    path(
        "v1/users/update",
        UpdateUserView.as_view(),
        name="update_user"
    ),
    path(
        "v1/users/me",
        GetUserDetailsView.as_view(),
        name="user_details"
    ),
]
