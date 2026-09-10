import traceback
# 암호화를 위해 임포트 해주었습니다.
from passlib.context import CryptContext

from fastapi import Request,Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlmodel import create_engine,Session,SQLModel
from fastapi import FastAPI,Depends
from fastapi.staticfiles import StaticFiles

from datetime import datetime

from sqlalchemy import text


from DTO.UserDTO import Member
from DTO.ReviewDTO import Review

app = FastAPI()
templates = Jinja2Templates(directory='templates/')  

DATABASE_URL = 'mysql+pymysql://root:human123$@127.0.0.1:3306/human'

engine = create_engine(DATABASE_URL,echo=True)


def get_session():
    with Session(engine) as session :
        yield session
        session.commit()

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

# 처음에 메인 주소
@app.get('/dsinside')
def main(request:Request):
    return templates.TemplateResponse(request,'main.html')

# 로그인 화면으로 넘어가는 곳 
@app.get('/login')
def login(request:Request):
    return templates.TemplateResponse(request,'login.html')


    
    

# 검색 후 넘어가는곳 
@app.get('/search')
def search(request:Request):
    return templates.TemplateResponse(request,'search.html')


# 현재는 id랑 pw가 같은지 비교하는 로직이 존재하지 않음
@app.post('/api/login')
def api_login(request:Request,
              member_id:str,
              member_pw : str):
    try:
        sql=text(
            '''
           select 
           member_id,
           member_pw
           from  member 
            '''
            
        )
        
    except Exception as e:
        pass

    return RedirectResponse(               
             url='/dsinside',
             status_code=303 # 303: 무조건 GET으로 다시 들어오게 한다
                   )

# 리뷰 수정을 하러 가는 곳
# 리뷰 수정을 하고 나서는 리뷰 수정한 내용을 보여주고 다시 원래 대로 돌아가는게 나을거같음
@app.get('/restaurant/update')   
def restaurantUpdate(request:Request):
    return templates.TemplateResponse(request,'update.html')

    
@app.get('/review/list')
def review(request:Request, 
        session:Session = Depends(get_session)):
    
    try:
        sql = text('''
                   select m.name, r.review_content, r.rating, r.review_time
                   from review as r join member as m using(member_code)
                   ''')
        
        result = session.exec(sql)
        review_list = result.mappings().fetchall()
        
    except Exception as e:
        print(e)
    
    return templates.TemplateResponse(request,'review.html', {
        'review_list': review_list
    })

@app.get('/review/add')
def review_add(request:Request):
    return templates.TemplateResponse(request,'review_add.html')

@app.post('/review/add')
def review_add2(
    review: Review =Form(),
    session:Session = Depends(get_session)
    ):
    print("/review/add 실행 성공")
    print("review:", review)
    
    sql = text('''
               insert into review (review_content, rating, review_time)
               values ( :review_content, :rating, :review_time)
               ''')
    
    session.exec(sql, {'review_content': review.review_content, 'rating': review.rating, 'review_time': datetime.now()})
    
    return RedirectResponse(
        url='/review/list',
        status_code=303
    )

# 회원 가입창 넘어가는 부분
@app.get('/signup')
def sing_up(request:Request):
    return templates.TemplateResponse(request,'sign_up.html')
    
@app.post('/api/signup')
def _signup():
    
    
    return RedirectResponse(               
        url='/dsinside',
        status_code=303 # 303: 무조건 GET으로 돌아오게 함
    )   
    
@app.get('/mypage')
def mypage(request:Request):
    return templates.TemplateResponse(request,'mypage.html')    








@app.get('/mypage/reviews')
def reviews(request:Request):
    
    return templates.TemplateResponse(request,'review_list.html')    


# ==================관리자 페이지 라우팅 ==================
# 전체 조회부터 되는지 테스트
@app.get('/manager')
def manager(
    request: Request,
    session: Session = Depends(get_session)
):
    
    
    try:
        sql = text('''
            SELECT * FROM member
        ''')
        result = session.exec(sql)
        member = result.mappings().fetchall()
        print(member)
        
    except Exception as e:
        print(f"데이터베이스 조회 중 에러 발생: {e}")
        
        
    return templates.TemplateResponse(
        request, 
        'admin_member.html',  
        {'member': member}
    )


# ==================상세 페이지 ==================   
@app.get('/detail')
def detail(
    request:Request,
    member_id:str,
    session:Session=Depends(get_session)
):
     
     try :
         sql=session.exec(text('''
            select *
            from member
            where member_id=:member_id            
         '''),params={'member_id':member_id})
        #  rows=result.fetchone()
     
         a=sql.mappings().fetchone()
       
         print('fetchone결과:',a)
       
         
           
     except Exception as e :
            print(e)        
    
    
     return templates.TemplateResponse(request,'detail.html',{'member':a})
                
    





# 서버 키는 곳
if __name__ == '__main__':
    import uvicorn
    uvicorn.run('api:app', port=8000, reload=True,host='0.0.0.0')