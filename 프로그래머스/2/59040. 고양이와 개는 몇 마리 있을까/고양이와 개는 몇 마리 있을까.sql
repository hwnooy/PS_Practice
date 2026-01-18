-- 코드를 입력하세요
SELECT ANIMAL_TYPE, COUNT(animal_id) AS COUNT from animal_ins
group by animal_type
ORDER BY ANIMAL_TYPE ASC