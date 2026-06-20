-- 코드를 입력하세요
/*
동물의 정보

들어온 동물 중 젊은 동물의 아이디와 이름을 조회
결과는 아이디 순으로 조회
*/
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION NOT LIKE 'Aged';