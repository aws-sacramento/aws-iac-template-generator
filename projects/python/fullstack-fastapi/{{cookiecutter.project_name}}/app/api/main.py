import uvicorn 
from functools import lru_cache 
from typing_extensions import Annotated 
from mangum import Mangum
from fastapi import Depends, FastAPI   
# Recommended to use starlette over FastAPI for CORS middleware
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

 
  
# Performance optimization for caching settings instead of loading env file every time.
@lru_cache
def get_settings():
    return config.Settings()
 
###############################################################################
#   CORS Middleware                                                      #
###############################################################################
origins = ["*"]
middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
] 
  
###############################################################################
#   Application object for the API                                            #
###############################################################################
app = FastAPI(
    middleware=middleware, # Recommended to inject middleware here instead referencing from app.add_middleware
    version="{{cookiecutter.app_version}}",
    title="{{cookiecutter.company_name}} {{cookiecutter.app_name}}",
    summary="Backend API for the {{cookiecutter.company_name}} {{cookiecutter.app_name}} application",
    contact={
        "name": "{{cookiecutter.company_name}}",
        "email": "{{cookiecutter.contact_email}}",
    }
    # -*- Examples for later
    # openapi_url=f"/api/v1/openapi.json",
    # docs_url="/api/docs", 
    # redoc_url="/api/redoc", 
    # swagger_ui_init_oauth=auth_provider.api_auth_scheme.init_oauth,
)

###############################################################################
#   Configure Routes                                                       #
###############################################################################


###############################################################################
#   GET API endpoints                                                         #
###############################################################################
@app.get("/")
async def root(settings: Annotated[config.Settings, Depends(get_settings)]):
    return {"success": True,  
            "app_environment": settings.env,
            "app_name": settings.app_name, 
            "app_version": settings.app_version, 
            "app_build_date": settings.app_build_date,
            "aws_region": settings.aws_region,
            "aws_dynamo_db_table_name": settings.aws_dynamo_db_table_name,
            "aws_access_key_id": settings.aws_access_key_id, 
            "aws_secret_access_key": settings.aws_secret_access_key
            }
 
###############################################################################
#   Handler for AWS Lambda                                                    #
###############################################################################
handler = Mangum(app)

###############################################################################
#   Run the self contained application                                        #
###############################################################################
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port={{cookiecutter.port_internal}})
