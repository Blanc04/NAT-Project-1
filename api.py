from fastapi import Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlmodel import create_engine, Session, SQLModel
from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles

from datetime import datetime
from sqlalchemy import text

from passlib.context import CryptContext
from DTO.ReviewDTO import Review
from DTO.MemberDTO import Member


# =========================================================
# FastAPI 기본 설정
# =========================================================

app = FastAPI()

templates = Jinja2Templates(directory='templates/')

DATABASE_URL = 'mysql+pymysql://root:human1234$@127.0.0.1:3306/human'

engine = create_engine(
    DATABASE_URL,
    echo=True
)


def get_session():
    with Session(engine) as session:
        yield session
        session.commit()


# =========================================================
# static 폴더 연결
# =========================================================

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# =========================================================
# 메인 페이지
# =========================================================

@app.get('/dsinside')
def main(request: Request):
    return templates.TemplateResponse(
        request,
        'main.html'
    )


# =========================================================
# 로그인 페이지
# =========================================================

@app.get('/login')
def login(request: Request):
    return templates.TemplateResponse(
        request,
        'login.html'
    )


# =========================================================
# 검색 페이지
# =========================================================

@app.get('/search')
def search(request: Request):
    return templates.TemplateResponse(
        request,
        'search.html'
    )


# =========================================================
# 로그인 처리
# 현재는 ID / PW 비교 로직 구현 전
# =========================================================

@app.post('/api/login')
def _login():
    try:
        pass

    except Exception as e:
        print('로그인 처리 에러:', e)

    return RedirectResponse(
        url='/dsinside',
        status_code=303
    )


# =========================================================
# 식당 정보 수정
# =========================================================

@app.get('/restaurant/update')
def restaurantUpdate(request: Request):
    return templates.TemplateResponse(
        request,
        'update.html'
    )


# =========================================================
# 리뷰 전체 조회
# =========================================================

@app.get('/review/list')
def review(
    request: Request,
    session: Session = Depends(get_session)
):
    review_list = []

    try:
        sql = text('''
            SELECT
                m.member_id,
                review_content,
                rating,
                DATE_FORMAT(review_time, "%Y.%m.%d") AS review_time
            FROM review AS r
            JOIN member AS m
            USING(member_code)
        ''')

        result = session.exec(sql)
        review_list = result.mappings().fetchall()

        print('리뷰 조회 결과:', review_list)

    except Exception as e:
        print('리뷰 조회 에러:', e)

    return templates.TemplateResponse(
        request,
        'review.html',
        {
            'review_list': review_list
        }
    )


# =========================================================
# 리뷰 작성 페이지
# =========================================================

@app.get('/review/add')
def review_add(request: Request):
    return templates.TemplateResponse(
        request,
        'review_add.html'
    )


@app.post('/review/add')
def review_add2(
    review: Review = Form(),
    session: Session = Depends(get_session)
):
    print("/review/add 실행 성공")
    print("review:", review)

    try:
        sql = text('''
            INSERT INTO review (
                review_content,
                rating,
                review_time
            )
            VALUES (
                :review_content,
                :rating,
                :review_time
            )
        ''')

        session.exec(
            sql,
            params={
                'review_content': review.review_content,
                'rating': review.rating,
                'review_time': datetime.now()
            }
        )

    except Exception as e:
        print('리뷰 등록 에러:', e)

    return RedirectResponse(
        url='/review/list',
        status_code=303
    )


# =========================================================
# 회원가입 페이지
# =========================================================

@app.get('/signup')
def sign_up(request: Request):
    return templates.TemplateResponse(
        request,
        'sign_up.html'
    )


# =========================================================
# 회원가입 처리
# =========================================================

ctx_pw = CryptContext(
    schemes=['argon2'],
    deprecated='auto'
)

def crypt(txt):
    return ctx_pw.hash(txt)

@app.post('/api/signup')
def _signup(
    member: Member = Form(),
    session: Session = Depends(get_session)
):
    print('/api/signup 실행 성공')
    print('member:', member)
    
    hashed = crypt(member.member_pw)
    
    try:
        sql = text('''
            INSERT INTO member (
                name,
                member_id,
                member_pw,
                member_pnum
            )
            VALUES (
                :name,
                :member_id,
                :member_pw,
                :member_pnum
            )
        ''')

        session.exec(
            sql,
            params={
                'name': member.name,
                'member_id': member.member_id,
                'member_pw': hashed,
                'member_pnum': member.member_pnum
            }
        )

    except Exception as e:
        print('회원가입 에러:', e)

    return RedirectResponse(
        url='/login',
        status_code=303
    )


# =========================================================
# 마이페이지
# =========================================================

@app.get('/mypage')
def mypage(request: Request):
    return templates.TemplateResponse(
        request,
        'mypage.html'
    )


@app.get('/mypage/reviews')
def reviews(request: Request):
    return templates.TemplateResponse(
        request,
        'review_list.html'
    )


# =========================================================
# 관리자 페이지
# 회원 전체 조회 및 관리
# =========================================================

@app.get('/manager')
def manager(
    request: Request,
    session: Session = Depends(get_session)
):
    member = []

    try:
        sql = text('''
            SELECT *
            FROM member
        ''')

        result = session.exec(sql)
        member = result.mappings().fetchall()

        print('회원 전체 조회:', member)

    except Exception as e:
        print(f"데이터베이스 조회 중 에러 발생: {e}")

    return templates.TemplateResponse(
        request,
        'admin_member.html',
        {
            'member': member
        }
    )


# =========================================================
# 관리자 페이지
# 회원 상세 조회
# =========================================================

@app.get('/detail')
def detail(
    request: Request,
    member_id: str,
    session: Session = Depends(get_session)
):
    member = None

    try:
        sql = text('''
            SELECT *
            FROM member
            WHERE member_id = :member_id
        ''')

        result = session.exec(
            sql,
            params={
                'member_id': member_id
            }
        )

        member = result.mappings().fetchone()

        print('fetchone 결과:', member)

    except Exception as e:
        print('상세조회 에러 발생:', e)

    return templates.TemplateResponse(
        request,
        'detail.html',
        {
            'member': member
        }
    )


# =========================================================
# 서버 실행
# =========================================================

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        'api:app',
        port=8000,
        reload=True,
        host='0.0.0.0'
    )