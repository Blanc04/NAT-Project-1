-- create table
create table Member(
member_code int auto_increment,
name varchar(20),
member_id varchar(12),
member_pw varchar(255),
member_pnum varchar(30),
admin_code int(2),
primary key(member_code)
)

create table Restaurant (
res_code int auto_increment,
member_code int(5),
category int(3),
res_name varchar(20),
rating decimal(1,1),
address varchar(50),
primary key(res_code),
foreign key(member_code) references Member(member_code)
)

create table Bookmark(
member_code int(5),
res_code int(5),
primary key(member_code, res_code),
foreign key(member_code) references Member(member_code),
foreign key(res_code) references Restaurant(res_code)
)

create table Menu(
menu_code int auto_increment,
res_code int(5),
menu_name varchar(20),
price int(10),
primary key(menu_code),
foreign key(res_code) references Restaurant(res_code)
)

create table Review(
review_code int auto_increment,
res_code int(5),
member_code int(5),
review_content varchar(40),
rating decimal(2,1),
review_time datetime,
primary key(review_code),
foreign key(res_code) references Restaurant(res_code),
foreign key(member_code) references Member(member_code)
)

create table Board(
board_code int auto_increment,
member_code int(5),
board_cate char(1),
board_title varchar(100),
board_content varchar(500),
view_count int(5),
board_time datetime,
primary key(board_code),
foreign key(member_code) references Member(member_code)
)

create table Comment(
comment_code int auto_increment,
board_code int(5),
member_code int(5),
comment_content varchar(40),
comment_time datetime,
primary key(comment_code),
foreign key(member_code) references Member(member_code),
foreign key(board_code) references Board(board_code)
)

create table Option_T(
option_code int auto_increment,
option_name varchar(20),
primary key(option_code)
)

create table ResOptionBridge(
res_code int(5),
option_code int(5),
primary key(res_code, option_code),
foreign key(res_code) references Restaurant(res_code),
foreign key(option_code) references Option_T(option_code)
)

create table Image(
img_code int auto_increment,
orig_imgname varchar(20),
arr_imgname varchar(40),
board_type int(1),
bcode int(5),
primary key(img_code)
)

-- 데이터 생성

INSERT INTO Member
(name, member_id, member_pw, member_pnum, admin_code)
VALUES
('김민수', 'minsu01', 'test1234', '010-1111-1111', 0),
('이서연', 'seoyeon02', 'test1234', '010-2222-2222', 0),
('박지훈', 'jihoon03', 'test1234', '010-3333-3333', 0),
('최유진', 'yujin04', 'test1234', '010-4444-4444', 0),
('관리자', 'admin01', 'admin1234', '010-5555-5555', 1);

INSERT INTO Restaurant
(member_code, category, res_name, rating, address)
VALUES
(6, 1, '서울맛집', 4.5, '서울특별시 종로구'),
(7, 2, '부산바다식당', 4.2, '부산광역시 해운대구'),
(8, 1, '대전칼국수', 4.8, '대전광역시 중구'),
(6, 3, '인천고기집', 4.0, '인천광역시 남동구'),
(9, 2, '수원분식당', 3.9, '경기도 수원시');

INSERT INTO Bookmark
(member_code, res_code)
VALUES
(6, 11),
(6, 13),
(7, 12),
(8, 11),
(9, 15);

INSERT INTO Menu
(res_code, menu_name, price)
VALUES
(11, '김치찌개', 8000),
(11, '제육볶음', 10000),
(12, '해물칼국수', 9000),
(13, '멸치칼국수', 7000),
(15, '떡볶이', 4000);

INSERT INTO Review
(res_code, member_code, review_content, rating)
VALUES
(11, 6, '음식이 정말 맛있어요.', 4.5),
(12, 7, '해물칼국수가 맛있습니다.', 4.2),
(13, 8, '국물이 정말 깔끔해요.', 4.8),
(11, 9, '가격 대비 괜찮은 식당입니다.', 4.0),
(15, 6, '떡볶이가 맛있어요.', 3.9);

INSERT INTO Board
(member_code, board_cate, board_title, board_content, view_count)
VALUES
(6, '1', '서울 맛집 추천해주세요', '종로 근처 맛집을 찾고 있습니다.', 15),
(7, '1', '부산 여행 맛집 공유', '부산에서 방문하기 좋은 맛집을 공유해주세요.', 32),
(8, '1', '대전 맛집 후기', '최근에 방문한 대전 맛집 후기입니다.', 21),
(9, '1', '인천 맛집 질문', '인천에서 고기 맛있는 곳이 있을까요?', 8),
(6, '1', '수원 맛집 추천', '수원역 근처 맛집 추천 부탁드립니다.', 17);

INSERT INTO Comment
(board_code, member_code, comment_content)
VALUES
(6, 7, '저도 그 식당 추천합니다.'),
(6, 8, '종로에 맛집이 정말 많아요.'),
(7, 6, '부산 여행 계획 중인데 참고하겠습니다.'),
(8, 9, '다음에 한번 방문해봐야겠네요.'),
(10, 7, '수원역 근처라면 저도 추천할 곳이 있습니다.');

INSERT INTO Option_T
(option_name)
VALUES
('주차 가능'),
('예약 가능'),
('포장 가능'),
('배달 가능'),
('단체석 가능');

INSERT INTO ResOptionBridge
(res_code, option_code)
VALUES
(11, 6),
(11, 8),
(12, 6),
(12, 7),
(13, 10);

INSERT INTO Image
(orig_imgname, arr_imgname, board_type, bcode)
VALUES
('food.jpg', 'food_001.jpg', 2, 6),
('restaurant.jpg', 'restaurant_001.jpg', 1, 12),
('review.jpg', 'review_001.jpg', 3, 6),
('menu.jpg', 'menu_001.jpg', 2, 11),
('store.jpg', 'store_001.jpg', 1, 13);

-- 작성시간 업데이트

UPDATE Review
SET review_time = '2026-09-01 10:30:00'
WHERE review_code = 6;

UPDATE Review
SET review_time = '2026-09-02 14:20:00'
WHERE review_code = 7;

UPDATE Review
SET review_time = '2026-09-03 11:45:00'
WHERE review_code = 8;

UPDATE Review
SET review_time = '2026-09-04 16:10:00'
WHERE review_code = 9;

UPDATE Review
SET review_time = '2026-09-05 18:35:00'
WHERE review_code = 10;

UPDATE Board
SET board_time = '2026-09-01 09:15:00'
WHERE board_code = 6;

UPDATE Board
SET board_time = '2026-09-02 13:40:00'
WHERE board_code = 7;

UPDATE Board
SET board_time = '2026-09-03 15:25:00'
WHERE board_code = 8;

UPDATE Board
SET board_time = '2026-09-04 17:50:00'
WHERE board_code = 9;

UPDATE Board
SET board_time = '2026-09-05 20:10:00'
WHERE board_code = 10;

UPDATE Comment
SET comment_time = '2026-09-01 11:00:00'
WHERE comment_code = 11;

UPDATE Comment
SET comment_time = '2026-09-01 11:20:00'
WHERE comment_code = 12;

UPDATE Comment
SET comment_time = '2026-09-02 14:00:00'
WHERE comment_code = 13;

UPDATE Comment
SET comment_time = '2026-09-03 16:30:00'
WHERE comment_code = 14;

UPDATE Comment
SET comment_time = '2026-09-05 20:30:00'
WHERE comment_code = 15;