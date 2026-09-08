const init = () => {
    bind()
}

window.onload = init

const bind = () => {
    const textarea = document.getElementById('review-content')
    const charCount = document.getElementById('char-count')
    const MAX_LENGTH = 1000

    textarea.addEventListener('input', () => {
        let currentLength = textarea.value.length

        // 1000자를 초과한 경우 처리
        if (currentLength > MAX_LENGTH) {
            // 1000자까지만 잘라내서 다시 입력창에 덮어쓰기
            textarea.value = textarea.value.slice(0, MAX_LENGTH)
            currentLength = MAX_LENGTH; // 카운트도 1000으로 고정

            // 사용자에게 알림
            alert('리뷰는 최대 1,000자까지만 작성할 수 있습니다.')
        }
        // 실시간 글자 수 업데이트
        charCount.textContent = `${currentLength} / 1,000자`
    })
}