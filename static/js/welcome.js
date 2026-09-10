
// 팝업창을 작동로직
// 웹 페이지가 로딩되면 팝업창의 내부 버튼을 찾아서 이벤트를 발생시킴
// 무조건 닫히는 경우, 7일간 안보기 클릭시 쿠키가 적용되는 구조
window.onload = () => {
    document.querySelector('.popup .close').addEventListener(
        'click', function (event) {

            console.log(event.target.parentElement.parentElement)

            event.target.parentElement.parentElement.classList.add('hide')
            if (event.target.parentElement.querySelector('.chk').checked) {
                document.cookie = `welcomePopup=True;  max-age=${60 * 60 * 24 * 7}; path=/`
            }
            
        }
    )
    value=getCookieValue('welcomePopup')

    if(value!=null){
        document.querySelector('.popup').classList.add('hide')
    }
   
}
/*
긴 문자열을 가져와서, 쿠키를 분리후 이름과 값을 분리하는 로직
*/
function getCookieValue(key){
    cookies=document.cookie.split('; ')
    for(cookie of cookies)
        
        names=cookie.split('=')[0]
        value=cookie.split('=')[1]

        if(names==key){
            return value
        }
        return null
}