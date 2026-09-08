from sqlmodel import SQLModel, Field

class Comme(SQLModel, table=True):
    comment_code : int | None = Field(
        default = None,
        primary_key = True
    )
    board_code : int = Field(
        foreign_key = 'Board.board_code'
    )
    user_code : int = Field(
        foreign_key = 'User.user_code'
    )
    comment_content : str