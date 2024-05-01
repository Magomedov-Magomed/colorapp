from users.models import User
from users.types import UserCreateData


class UserService:

    def create_user(self, user_data: UserCreateData) -> User:
        user = User.objects.create_user(**user_data)
        return user
