from typing import Optional

from pydantic import BaseModel, Field


# Expenses = Actual data/object
class Expenses:
    id: int
    name: str
    ammount: int

    def __init__(self, id, name, ammount):
        self.id = id
        self.name = name
        self.ammount = ammount


# ExpenseRequest = what the client is allowed to send
class ExpenseRequest(BaseModel):
    # id: Optional[int] = Field(description="ID is not needed", default=None)
    name: str = Field(min_length=1, max_length=50)
    ammount: int = Field(gt=0, lt=20000)

    model_config = {
        "json_schema_extra": {"example": {"name": "expense name", "ammount": 1}}
    }
