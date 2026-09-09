from sqlmodel import SQLModel, Field
from datetime import datetime

class Comment(SQLModel, table=True):
    comment_code : int | None = Field(
        default = None,
        primary_key = True
    )
    board_code : int = Field(
        foreign_key = 'Board.board_code'
    )
    member_code : int = Field(
        foreign_key = 'Member.member_code'
    )
    comment_content : str
    comment_time : str = datetime.now()