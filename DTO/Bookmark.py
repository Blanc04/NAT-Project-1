from sqlmodel import SQLModel, Field

class Bookmark(SQLModel, table=True):
    user_code : int | None = Field(
        default = None,
        primary_key = True,
        foreign_key = 'User.user_code'
    )
    res_code : int = Field(
            default = None,
            primary_key = True,
            foreign_key='Resta.res_code'
        )