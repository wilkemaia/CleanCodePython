from .user_creator import UserCreator
import pytest
class UserRepositoryMock:
    def __init__(self):
        self.select_user_att ={}
        self.insert_user_att ={}
    def select_user(self,person_name:str) -> list:
        self.select_user_att["person_name"] = person_name
        return []
    
    def insert_user(self,person:str,age:int,height: float) -> None:
        self.insert_user_att["person_name"] = person
        self.insert_user_att["age"] = age
        self.insert_user_att["height"] = height
        
        
        
class UserRepositoryMockWithErro:
    def __init__(self):
        self.insert_user_att ={}
    def select_user(self,person_name:str) -> list:
        self.insert_user_att["person_name"] = person_name
        return [1,2,3]
  
def test_insert_new_user():
        user_repository = UserRepositoryMock()
        user_creator = UserCreator(user_repository)
            
        person_name ="Wilke"
        age = 48
        height = 1.80
        
        
        response =  user_creator.insert_new_user(person_name,age,height)
        assert user_repository.select_user_att["person_name"] == person_name
        assert user_repository.insert_user_att["age"] == 48
        assert user_repository.insert_user_att["height"] == 1.80
        
        assert isinstance(response,dict)
        assert response["Count"] == 1
        assert response["Message"] =="Usuário cadastrado com sucesso.!"
        
def test_insert_new_user_with_error():
    user_repository = UserRepositoryMockWithErro()
    user_creator = UserCreator(user_repository)
    
    with pytest.raises(Exception) as  exc_info:
         user_creator.insert_new_user("somenthing",38,1.78)
    assert str(exc_info.value) =="Usuário já cadastrado"