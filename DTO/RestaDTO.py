from sqlmodel import SQLModel, Field
from typing import Optional

class Resta(SQLModel, table=True):
	res_code : int | None = Field(
		default = None,
		primary_key = True
	)
	user_code : int = Field(
        foreign_key='User.user_code'
    )
	category : str
	res_name : str
	rating	 : Optional[float]
	address  : str