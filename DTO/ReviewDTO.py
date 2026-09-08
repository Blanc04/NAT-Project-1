from sqlmodel import SQLModel, Field
from typing import Optional

class Review(SQLModel, table=True):
    review_code : int | None = Field(
        default = None,
        primary_key = True
    )
    res_code : int = Field(
        foreign_key = 'Restaurant.res_code'
    )
    member_code : int = Field(
        foreign_key = 'Member.member_code'
    )
    review_content : str
    rating : Optional[float]