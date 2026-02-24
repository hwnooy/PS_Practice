-- 코드를 입력하세요
SELECT aout.animal_id as animal_id, aout.name as name
from animal_outs as aout left join animal_ins as ain 
on aout.animal_id=ain.animal_id
where ain.sex_upon_intake is null
order by aout.animal_id 