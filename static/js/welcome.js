
// 팝업창을 작동로직
// 무조건 닫히는 경우, 7일간 안보기 클릭시 쿠키가 적용되는 구조
window.onload=()=>{
    document.querySelector('.popup .close').addEventListener(
        'click',function(event){
            console.log(event.target.parentElement.parentElement)
            event.target.parentElement.parentElement.classList.add('hide')
            if(event.target.parentElement.querySelector('.chk').checked){
                document.cookie='welcomePopup; max-age=10'
            }
        }
        // 쿠키 먹이는 부분
    
    )
//   max-age가 만료일이며, 단위는 초
}