-- 코드를 입력하세요
SELECT distinct(comp.car_id) as car_id 
from car_rental_company_car as comp join car_rental_company_rental_history as his
on comp.car_id = his.car_id 
where car_type = '세단' and his.start_date like '%-10-%'
order by car_id desc