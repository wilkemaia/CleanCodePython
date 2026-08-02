from src.Views.http_types.http_response import HttpResponse
from .errors_type.http_not_found import HttpNotFoundError

def handle_errors(error:Exception) -> HttpResponse:
    if isinstance(error,(HttpNotFoundError)):
        return HttpResponse (
            status_code = error.status_code,
            body={
               "error" : [{
                   "title":error.name,
                   "detail":error.message
               }
                    
                ]
            }
            
        )
    
    return HttpResponse (
                status_code = error.status_code,
                body={
                   "error" : [{
                       "title":"Server error",
                       "detail":str(error)
                   }
                        
                    ]
                }
                
            )