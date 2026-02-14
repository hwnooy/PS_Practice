-- 코드를 입력하세요
SELECT food_type, rest_id, rest_name,favorites
from (
    select *,
    row_number() over(
    partition by food_type order by favorites desc) as rn
    from rest_info
) t
where rn=1
order by food_type desc