from src.models.entities.users  import Users
from .user_finder import UserFinder

class UserRepositoryMock:
    def __init__(self):
        self.select_user_att = {}
        
    
    def  select_user(self,person_name:str)-> list:
        self.select_user_att["person_name"] = person_name
        return[
            Users(
                id = 123,
                person_name= "Mock_persona",
                age = 78,
                height =1.80
            )
        ]
        
def test_find_by_person_name():
    person_name = "my_person_name"
    user_repo = UserRepositoryMock()
    user_finder = UserFinder(user_repo)
    
    response  =  user_finder.find_by_persona_name(person_name)
    print(user_repo.select_user_att)
    print(response)
    
    assert user_repo.select_user_att["person_name"] ==person_name
    assert isinstance(response,dict)
    assert response["Type"] == "Users"
    assert "attributes" in response
    assert isinstance(response["attributes"],list)
