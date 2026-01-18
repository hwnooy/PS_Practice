-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME,
CASE 
    WHEN SEX_UPON_INTAKE like '%Neutered%' THEN'O'
    when sex_upon_intake like '%Spayed%' then 'O'
    else 'X'
end AS '중성화' 
FROM ANIMAL_INS
ORDER BY ANIMAL_ID 
