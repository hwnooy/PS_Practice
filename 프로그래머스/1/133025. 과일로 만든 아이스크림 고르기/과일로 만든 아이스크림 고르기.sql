-- 코드를 입력하세요
SELECT fh.flavor
from first_half as fh join icecream_info as info on fh.flavor = info.flavor
where info.ingredient_type = 'fruit_based' and fh.total_order>3000