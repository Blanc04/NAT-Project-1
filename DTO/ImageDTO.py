from sqlmodel import SQLModel, Field

class Image(SQLModel, table=True):
    img_code : int | None = Field(
        default = None,
        primary_key = True
    )
    orig_imgname : str
    arr_imgname : str
    board_type : int
    bcode : int