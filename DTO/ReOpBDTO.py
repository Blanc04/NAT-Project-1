from sqlmodel import SQLModel, Field

class ReOpB(SQLModel, table=True):
    res_code : int | None = Field(
        default = None,
        primary_key = True,
        foreign_key = 'Resta.res_code'
    )
    option_code : int | None = Field(
        default = None,
        primary_key = True,
        foreign_key = 'Option.option_code'
    )