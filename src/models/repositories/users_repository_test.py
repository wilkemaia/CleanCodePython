from src.models.connection.db_connection_handler import DbConnectionHandler
from .users_repository import UsersRepository
import pytest
@pytest.mark.skip(reason="insert in DB")
def test_users_repository():
    db_conn = DbConnectionHandler()
    use_repo =  UsersRepository(db_conn)
    
    person_name = "Wilke3"
    age = 88
    height = 1.78
    users =  use_repo.select_user(person_name)
    #print(users)
    assert isinstance(users, list)
    assert len(users) ==1
    assert users[0].person_name == person_name
    assert users[0].age ==88
   # use_repo.insert_user(person_name,age,height)

#para testar no terminal 
# pytest -s -v src/models/repositories/users_repository_test.py