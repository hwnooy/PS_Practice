-- 코드를 입력하세요
SELECT fp.product_id, fp.product_name, sum(fp.price*amount) as total_sales
from food_product as fp join food_order as fo on fp.product_id = fo.product_id
where fo.produce_date like '2022-05-%'
group by fp.product_id
order by total_sales desc, product_id asc