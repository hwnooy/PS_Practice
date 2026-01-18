-- 코드를 입력하세요
-- 진료과가 cs 또는 gs인 의사이름, 의사 id, 진료과, 고용일자 ,
-- 고용일자 기준 내림차순, 고용일자가 같으면 이름기준 오름차순 
SELECT DR_NAME, DR_ID, MCDP_CD, DATE_FORMAT(HIRE_YMD, '%Y-%m-%d') FROM DOCTOR 
WHERE MCDP_CD = 'GS' OR MCDP_CD = 'CS'
ORDER BY HIRE_YMD DESC, DR_NAME ASC