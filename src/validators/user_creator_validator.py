from pydantic import BaseModel,constr,ValidationError
from src.errors.errors_type.http_unprocessable_entity import HttpunprocessaAbleEntity
def user_creator_validator(http_request:any)->None:
    class BodyData(BaseModel):
        person_name:constr(min_length=1) # type: ignore 
        age:int
        height:float
    
    try:
        BodyData(**http_request.body)
    except ValidationError as error:
        raise HttpunprocessaAbleEntity(error.errors()) from error
        
        
    