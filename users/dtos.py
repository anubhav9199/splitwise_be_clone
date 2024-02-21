from rest_framework import serializers

from users.models import User


class UserSignInSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'password'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UpdateUserInfoSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False, default="")
    last_name = serializers.CharField(required=False, default="")
    phone_number = serializers.CharField(required=False, default="")
    