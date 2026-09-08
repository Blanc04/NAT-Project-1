from sqlmodel import SQLModel, Field

class Menu(SQLModel, table=True):
    menu_code : int | None = Field(
        default = None,
        primary_key = True
    )
    menu_name : str
    price : int