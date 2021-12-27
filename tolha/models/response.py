from pydantic import BaseModel
from fastapi_utils.api_model import APIModel


class BaseResponse(APIModel):
    result_code: int
    result_desc: str
    developer_message: str