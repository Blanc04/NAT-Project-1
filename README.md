# NAT-Project-1

맛집을 검색하고 추천받으며, 직접 리뷰와 북마크를 남길 수 있는  
**맛집 추천 및 리뷰 웹 서비스 팀 프로젝트**입니다.

---

## 📅 프로젝트 기간

- 시작일: 2026-08-31

---

## 📌 프로젝트 소개

사용자가 다양한 맛집 정보를 확인하고 직접 리뷰를 작성할 수 있는 웹 서비스입니다.

회원 기능을 기반으로 맛집 검색, 리뷰 작성, 북마크, 지도 등의 기능을 제공하며  
각 기능을 팀원별 Git 브랜치로 분리하여 개발합니다.

---

## ✨ 주요 기능

### 👤 회원
- 회원가입
- 로그인
- 로그아웃
- 회원정보 수정
- 마이페이지

### 🍽️ 맛집
- 맛집 등록
- 맛집 조회
- 맛집 수정
- 맛집 검색

### ⭐ 리뷰
- 리뷰 목록 조회
- 리뷰 작성
- 리뷰 수정
- 리뷰 삭제

### 🔖 북마크
- 맛집 북마크 추가
- 북마크 삭제
- 북마크 목록 조회

### 🗺️ 지도
- 맛집 위치 확인
- 지도 기반 맛집 정보 제공

---

## 🛠️ 기술 스택

### Frontend
- HTML
- CSS
- JavaScript
- Jinja2

### Backend
- Python
- FastAPI

### Database
- MySQL
- SQLModel

### Collaboration
- Git
- GitHub
- SourceTree

---

## 🌿 Git Branch

```text
main
│
├─ feature/auth
│   └─ 로그인 / 회원가입 / 로그아웃
│
├─ feature/mypage
│   └─ 마이페이지 / 회원정보 수정
│
├─ feature/restaurant
│   └─ 맛집 등록 / 조회 / 수정
│
├─ feature/review
│   └─ 리뷰 목록 / 작성 / 수정 / 삭제
│
├─ feature/bookmark
│   └─ 북마크 추가 / 삭제 / 조회
│
├─ feature/search
│   └─ 맛집 검색
│
└─ feature/map
    └─ 지도 기능
