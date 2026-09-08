from sqlmodel import SQLModel, Field

class Option_T(SQLModel, table=True):
    option_code : int | None = Field(
        default = None,
        primary_key = True
    )
    option_name : str