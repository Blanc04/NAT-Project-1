from sqlmodel import SQLModel, Field

class Board(SQLModel, table=True):
    board_code : int | None = Field(
        default = None,
        primary_key = True
    )
    member_code : int = Field(
            foreign_key='Member.member_code'
        )
    board_cate : str
    board_title : str
    board_content : str
    view_count : int