from django.urls import path

from splitwise.views import UserExpenseView, UserPaymentDashboardView, UserSettelmentView


urlpatterns = [
    path(
        "v1/payment/dashboard",
        UserPaymentDashboardView.as_view(),
        name="user_sign_in",
    ),
    path(
        "v1/payment/expense/create",
        UserExpenseView.as_view(),
        name="add_expence"
    ),
    path(
        "v1/payment/expense/update/<str:payment_id>",
        UserExpenseView.as_view(),
        name="update_expense",
    ),
    path(
        "v1/payment/expense/delete/<str:payment_id>",
        UserExpenseView.as_view(),
        name="delete_expense",
    ),
    path(
        "v1/payment/settlement/<str:owe_payment_id>",
        UserSettelmentView.as_view(),
        name="user_owe_payment_settlement",
    ),
]