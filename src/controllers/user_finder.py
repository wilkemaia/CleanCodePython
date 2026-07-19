from src.models.repositories.interfaces.users_repository import UserRepositoryInterface
from .interfaces.user_finder import UserFinderInterface
class UserFinder(UserFinderInterface):
    def __init__(self,users_repository: UserRepositoryInterface):
        self.__users_repo = users_repository
        
    def  find_by_person_name(self,person_name:str)-> dict:
        selected_users = self.__select_and_validate_user(person_name)
        return self.__format_response(selected_users)
    
    def __select_and_validate_user(self,person_name:str) ->list:
        selected_use = self.__users_repo.select_user(person_name)
        
        if (not selected_use or len(selected_use))==0:
            raise Exception("Usuário não encontrado.!")
        
        return  selected_use
    
    
    def __format_response(self, selected_users:list) -> list:
        formatted_users = []
        for users in selected_users:
            formatted_users.append({
                "id":users.id,
                "person_name":users.person_name,
                "age":users.age,
                "height": users.height
            })
            
            return {
                "Type":"Users",
                "count":len(formatted_users),
                "attributes":formatted_users
            }
        
    
    
            