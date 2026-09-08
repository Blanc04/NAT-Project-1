from sqlmodel import SQLModel, Field
from typing import Optional

class Revie(SQLModel, table=True):
    review_code : int | None = Field(
        default = None,
        primary_key = True
    )
    res_code : int = Field(
        foreign_key = 'Resta.res_code'
    )
    user_code : int = Field(
        foreign_key = 'User.user_code'
    )
    review_content : str
    rating : Optional[float]