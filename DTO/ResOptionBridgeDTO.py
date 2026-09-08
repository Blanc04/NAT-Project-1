from sqlmodel import SQLModel, Field

class ResOptionBridge(SQLModel, table=True):
    res_code : int | None = Field(
        default = None,
        primary_key = True,
        foreign_key = 'Restaurant.res_code'
    )
    option_code : int | None = Field(
        default = None,
        primary_key = True,
        foreign_key = 'Option.option_code'
    )