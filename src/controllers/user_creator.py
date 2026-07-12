from src.models.repositories.interfaces.users_repository import UserRepositoryInterface

class UserCreator:
    def __init__(self,users_repository:UserRepositoryInterface):# Inverção da dependência
        self.__user_repo = users_repository
        
        
    def insert_new_user(self,person_name:str,age:int,height: float)-> dict:
        self.__check_if_user_exist(person_name)
        self.__create_new_user(person_name,age,height)
        return  self.__format_response()
    
    def __check_if_user_exist(self,person_name:str) ->None:
        select_user = self.__user_repo.select_user(person_name)
        if (not select_user or len(select_user)==0) :
            return
        raise Exception("Usuário já cadastrado")
    
    
    def __create_new_user(self,person_name:str,age:int,height:float)->None:
        self.__user_repo.insert_user(person_name,age,height)
        
    
    def __format_response(self)-> dict:
        return {
            "Type":"Users",
            "Count":1,
            "Message":"Usuário cadastrado com sucesso.!"
        }