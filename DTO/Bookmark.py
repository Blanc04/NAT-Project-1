from sqlmodel import SQLModel, Field

class Bookmark(SQLModel, table=True):
    member_code : int | None = Field(
        default = None,
        primary_key = True,
        foreign_key = 'Member.member_code'
    )
    res_code : int = Field(
            default = None,
            primary_key = True,
            foreign_key='Restaurant.res_code'
        )