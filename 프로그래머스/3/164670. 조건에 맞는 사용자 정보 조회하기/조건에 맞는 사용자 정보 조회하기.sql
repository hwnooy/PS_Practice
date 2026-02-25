-- 코드를 입력하세요
SELECT user_id, nickname, concat(city, " ", street_address1, " ", street_address2) as 전체주소, concat_ws("-", left(tlno,3), substring(tlno,4,4), substring(tlno,8,4)) as 전화번호 
from used_goods_board as goods join used_goods_user as users
on goods.writer_id = users.user_id
group by goods.writer_id
having count(*)>=3
order by users.user_id desc 
-- select * from used_goods_board