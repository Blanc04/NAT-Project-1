from fastapi import Request,Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlmodel import create_engine,Session,SQLModel
from fastapi import FastAPI,Depends
from fastapi.staticfiles import StaticFiles


app = FastAPI()
templates = Jinja2Templates(directory='templates/')  


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

# 검색후 넘어가는곳 


@app.get('/search')
def search(request:Request):
 return templates.TemplateResponse(request,'search.html')


# 현재는 id랑 pw가 같은지 비교하는 로직이 존재하지 않음

@app.post('/api/login')
def _login():
    try:
        pass
    except:
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
def review(request:Request):
     return templates.TemplateResponse(request,'review.html')


# 회원 가입창 넘어가는 부분
@app.get('/signup')
def sing_up(request:Request):
 return templates.TemplateResponse(request,'sign_up.html')
    
@app.post('/api/signup')
def _signup():
    
    
 return RedirectResponse(               
    url='/bap',
    status_code=303 # 303: 무조건 GET으로 돌아오게 함
                   )   
    
@app.get('/mypage')
def mypage(request:Request):
 return templates.TemplateResponse(request,'mypage.html')    








@app.get('/mypage/reviews')
def reviews(request:Request):
    
 return templates.TemplateResponse(request,'review_list.html')    








# 서버 키는 곳
if __name__ == '__main__':
 import uvicorn
 uvicorn.run('api:app', port=8000, reload=True,host='0.0.0.0')