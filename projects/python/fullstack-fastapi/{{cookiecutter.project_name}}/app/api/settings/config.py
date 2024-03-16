from fastapi.responses import JSONResponse
from pydantic_settings import BaseSettings, SettingsConfigDict


def getResponseWithHeaders(content: any, http_method: str = "*", status_code: int = 200) -> dict:
 
    """
    Returns a response with required headers and status code. 
    This is required for AWS Lambda functions with AWS API Gateway proxy.

    Parameters:
    - content: The content to be returned in the response body.
    - http_method: The HTTP method used for the request. Default is "*".
    - status_code: The status code to be returned in the response. Default is 200.

    Returns:
    - A JSONResponse object with the specified content, headers, and status code.

    Example Usage:
    response = getResponseWithHeaders(content={"message": "Success"}, http_method="POST", status_code=201)
    """
   
    match http_method:
        case 'POST':
            status_code = 201 
        case _:
            status_code = 200
         
    
    headers =  {
        "Access-Control-Allow-Headers" : "authorizationToken,Content-Type,X-Amz-Date,X-Amz-Security-Token,Authorization,X-Api-Key,X-Requested-With,Accept,Access-Control-Allow-Methods,Access-Control-Allow-Origin,Access-Control-Allow-Headers,*",
        "Access-Control-Allow-Origin": "*", # Allow from anywhere 
        "Access-Control-Allow-Methods":  "*", #f"${http_method}" # Allow only GET request 
    }
    
    return JSONResponse(content=content, headers=headers, status_code=status_code)

class Settings(BaseSettings):
    env: str = ""
    app_name: str = ""
    app_version: str = ""
    app_build_date: str = ""

    # AWS Access
    aws_access_key_id: str = ""
    aws_secret_access_key: str = ""
    aws_auth_token: str = ""
    aws_region: str = ""
  
    # Dynamo DB
    aws_dynamo_db_table_name: str = "" 
 
    model_config = SettingsConfigDict(env_file=('app/api/.env'))

    # -*- Use if hierarchy of environment variable files is required.
    # model_config = SettingsConfigDict(env_file=('app/api/.env', f'.env.development'))
