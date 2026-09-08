from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
	user_code : int | None = Field(
		default = None,
		primary_key = True
	)
	name : str
	user_id : str
	user_pw : str
	user_pnum : str
	admin_code : int