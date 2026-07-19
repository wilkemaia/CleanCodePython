from src.models.entities.users  import Users
from .user_finder import UserFinder


class User:
    def __init__(self, id, person_name, age, height):
        self.id = id
        self.person_name = person_name
        self.age = age
        self.height = height
class UserRepositoryMock:
    def __init__(self):
        self.select_user_att = {}
         
    def  select_user(self,person_name:str)-> list:
        self.select_user_att["person_name"] = person_name
        return [
            Users(
                 123,
                 "Mock_persona",
                 78,
                1.80
            )
        ]
        
def test_find_by_person_name():
    person_name = "my_person_name"
    user_repo = UserRepositoryMock()
    user_finder = UserFinder(user_repo)
    
    response  =  user_finder.find_by_person_name(person_name)
    print(user_repo.select_user_att)
    print(response)
    
    assert user_repo.select_user_att["person_name"] ==person_name
    assert isinstance(response,dict)
    assert response["Type"] == "Users"
    assert "attributes" in response
    assert isinstance(response["attributes"],list)
