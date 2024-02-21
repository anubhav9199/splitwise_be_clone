

from users.exceptions import UserNotFoundException
from users.models import User


class UserDbService:
    @staticmethod
    def get_user(email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise UserNotFoundException(
                f"User not found with email: {email}."
            )

    @staticmethod
    def update_user(user_id, data_to_update):
        return User.objects.filter(id=user_id).update(**data_to_update)
