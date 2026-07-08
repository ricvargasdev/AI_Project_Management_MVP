from pydantic import BaseModel
from pydantic import ConfigDict


class CustomerResponse(BaseModel):

    id: int
    name: str

    model_config = ConfigDict(
        from_attributes=True
    )