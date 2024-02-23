from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from common.constants import SUCCESS


class UserPaymentDashboardView(APIView):
    def get(self, request):
        return Response(
            {
                "status": SUCCESS,
                "detail": {}
            },
            status=status.HTTP_200_OK
        )


class UserExpenseView(APIView):
    
    def post(self, request):
        return Response(
            {
                "status": SUCCESS,
                "detail": {}
            },
            status=status.HTTP_201_CREATED
        )

    def patch(self, request, payment_id) -> Response:
        return Response(
            {
                "status": SUCCESS,
                "detail": {}
            },
            status=status.HTTP_200_OK
        )

    def delete(self, request, payment_id):
        return Response(
            {
                "status": SUCCESS,
                "detail": {}
            },
            status=status.HTTP_200_OK
        )


class UserSettelmentView(APIView):
    def patch(self, request, owe_payment_id):
        return Response(
            {
                "status": SUCCESS,
                "detail": {}
            },
            status=status.HTTP_200_OK
        )
