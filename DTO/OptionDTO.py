from sqlmodel import SQLModel, Field

class Option(SQLModel, table=True):
    option_code : int | None = Field(
        default = None,
        primary_key = True
    )
    option_name : str