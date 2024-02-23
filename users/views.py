from django.http import JsonResponse
from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from common.constants import (
    ERROR,
    SUCCESS
)
from common.utils import ErrorFormat

from users.crud import UserDbService
from users.dtos import (
    UpdateUserInfoSerializer,
    UserSignInSerializer,
    UserSignUpSerializer
)
from users.exceptions import UserNotFoundException
from users.serializers import UserDataSerializer


def custom404(request, exception=None):
    return JsonResponse(
        data={"status": "error", "detail": "Please check the url"},
        status=status.HTTP_404_NOT_FOUND,
    )


class UserSignInView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        params = UserSignInSerializer(data=request.data)
        if not params.is_valid():
            return Response(
                data={
                    "status": ERROR,
                    "detail": ErrorFormat.get_formated(params.errors),
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user = None
        request_body = params.data
        email = request_body["email"] # type: ignore
        password = request_body["password"] # type: ignore

        try:
            user = UserDbService.get_user(email=email)
        except UserNotFoundException:
            pass

        if not user:
            user = authenticate(username=email, password=password)
        
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "status": SUCCESS,
                    "detail": {
                        "token": token.key,
                        "email": email
                    }
                },
                status=status.HTTP_200_OK
            )

        return Response(
            {
                "status": ERROR,
                "detail": "Invalid credentials"
            },
            status=status.HTTP_401_UNAUTHORIZED
        )


class UserSignUpView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        params = UserSignUpSerializer(data=request.data)
        if not params.is_valid():
            return Response(
                data={
                    "status": ERROR,
                    "detail": ErrorFormat.get_formated(params.errors),
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        params.save()
        return Response(
            {
                "status": SUCCESS,
                "detail": params.data
            },
            status=status.HTTP_201_CREATED
        )


class UpdateUserView(APIView):
    def post(self, request):
        params = UpdateUserInfoSerializer(data=request.data)
        user = request.user
        if not params.is_valid():
            return Response(
                data={
                    "status": ERROR,
                    "detail": ErrorFormat.get_formated(params.errors),
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        request_body = params.data
        data_to_update = {
            key: params.data[key]
            for key in request_body
            if request_body.get(key) # type: ignore
        }
        user = UserDbService.update_user(user.id, data_to_update)

        return Response(
            data={
                "status": SUCCESS,
                "detail": {
                    "user": UserDataSerializer(user).data
                },
            },
            status=status.HTTP_200_OK,
        )


class GetUserDetailsView(APIView):
    def get(self, request):
        return Response(
            {
                "status": SUCCESS,
                "detail": {
                    "user": UserDataSerializer(request.user).data
                },
            },
            status=status.HTTP_200_OK,
        )


class UserLogoutView(APIView):
    def get(self, request):
        try:
            request.user.auth_token.delete()
            return Response(
                {
                    "status": SUCCESS,
                    "detail": "Successfully logged out."
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {
                    "status": SUCCESS,
                    "detail": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
