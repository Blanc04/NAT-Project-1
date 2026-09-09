from sqlmodel import SQLModel, Field

class Member(SQLModel, table=True):
	member_code : int | None = Field(
		default = None,
		primary_key = True
	)
	name : str
	member_id : str
	member_pw : str
	member_pnum : str
	admin_code : int