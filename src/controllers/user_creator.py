from src.models.repositories.interfaces.users_repository import UserRepositoryInterface

class UserCreator:
    def __init__(self,users_repository:UserRepositoryInterface):# Inverção da dependência
        self.__user_repo = users_repository