from pydantic import BaseModel, HttpUrl

class BaseResponse(BaseModel):
    success: bool = True
    status_code: int = 200
    message: str = "Success"
    data: dict

class BaseResponseList(BaseModel):
    success: bool = True
    status_code: int = 200
    message: str = "Success"
    data: list