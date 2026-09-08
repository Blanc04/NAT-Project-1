from sqlmodel import SQLModel, Field
from typing import Optional

class Restaurant(SQLModel, table=True):
	res_code : int | None = Field(
		default = None,
		primary_key = True
	)
	member_code : int = Field(
        foreign_key='Member.member_code'
    )
	category : str
	res_name : str
	rating	 : Optional[float]
	address  : str